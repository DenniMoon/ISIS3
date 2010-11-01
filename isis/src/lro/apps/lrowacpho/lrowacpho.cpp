// $Id$
#include "Isis.h"

#include <string>
#include "ProcessByLine.h"
#include "SpecialPixel.h"
#include "Hillier.h"
#include "PhotometricFunction.h"
#include "Exponential.h"
#include "HapkeExponential.h"
#include "Pvl.h"
#include "Cube.h"

#include "PvlGroup.h"
#include "iException.h"

using namespace std;
using namespace Isis;

// Global variables
PhotometricFunction *pho;

void phoCal ( Buffer &in, Buffer &out );
void phoCalWithBackplane ( std::vector<Isis::Buffer *> &in, std::vector<Isis::Buffer *> &out );

void IsisMain () {
    // We will be processing by line
    ProcessByLine p;

    // Set up the input cube and get camera information
    Cube *icube = p.SetInputCube("FROM");

    // Create the output cube
    Cube *ocube = p.SetOutputCube("TO");

    // Set up the user interface
    UserInterface &ui = Application::GetUserInterface();

    bool useBackplane = false;

    if (ui.WasEntered("BACKPLANE")) {
        CubeAttributeInput backplaneCai = ui.GetInputAttribute("BACKPLANE");

        if ( backplaneCai.Bands().size() != 3 ) {
            string msg = "Invalid Backplane: The backplane must be exactly 3 bands";
            throw iException::Message(iException::User, msg, _FILEINFO_);
        }

        if (icube->Bands() != 1) {
            string msg = "Invalid Image: The backplane option can only be used with a single image band at a time.";
            throw iException::Message(iException::User, msg, _FILEINFO_);
        }

        CubeAttributeInput cai;
        cai.Set("+" + backplaneCai.Bands()[0]);
        p.SetInputCube(ui.GetFilename("BACKPLANE"), cai);
        cai.Reset();
        cai.Set("+" + backplaneCai.Bands()[1]);
        p.SetInputCube(ui.GetFilename("BACKPLANE"), cai);
        cai.Reset();
        cai.Set("+" + backplaneCai.Bands()[2]);
        p.SetInputCube(ui.GetFilename("BACKPLANE"), cai);

        useBackplane = true;
    }

    // Get the name of the parameter file
    Pvl par(ui.GetFilename("PHOPAR"));

    iString algoName = PhotometricFunction::AlgorithmName(par);
    algoName.UpCase();

    if (algoName == "HILLIER") {
        pho = new Hillier(par, *icube, !useBackplane);
    }
    else if (algoName == "EXPONENTIAL") {
        pho = new Exponential(par, *icube, !useBackplane);
    }
    else if (algoName == "HAPKEEXPONENTIAL") {
        pho = new HapkeExponential(par, *icube, !useBackplane);
    }
    else {
        string msg = " Algorithm Name [" + algoName + "] not recognized. ";
        msg += "Compatible Algorithms are:\n    Hillier\n    Exponential\n    HapkeExponential";

        throw iException::Message(iException::User, msg, _FILEINFO_);
    }

    pho->SetMinimumPhaseAngle(ui.GetDouble("MINPHASE"));
    pho->SetMaximumPhaseAngle(ui.GetDouble("MAXPHASE"));
    pho->SetMinimumEmissionAngle(ui.GetDouble("MINEMISSION"));
    pho->SetMaximumEmissionAngle(ui.GetDouble("MAXEMISSION"));
    pho->SetMinimumIncidenceAngle(ui.GetDouble("MININCIDENCE"));
    pho->SetMaximumIncidenceAngle(ui.GetDouble("MAXINCIDENCE"));

    // Start the processing
    if (useBackplane)
        p.StartProcess(phoCalWithBackplane);
    else
        p.StartProcess(phoCal);

    PvlGroup photo("Photometry");
    pho->Report(photo);
    ocube->PutGroup(photo);
    Application::Log(photo);
    p.EndProcess();
}

/**
 * @brief Apply Hillier photometric correction
 *
 * Short function dispatched for each line to apply the Hillier photometrc
 * correction function.
 *
 * @author kbecker (2/20/2010)
 *
 * @param in Buffer containing input data
 * @param out Buffer of photometrically corrected data
 */
void phoCal ( Buffer &in, Buffer &out ) {

    for (int i = 0; i < in.size(); i++) {
        //  Don't correct special pixels
        if (IsSpecial(in[i])) {
            out[i] = in[i];
        }
        else {
            // Get correction and test for validity
            double ph = pho->Compute(in.Line(i), in.Sample(i), in.Band(i));
            out[i] = (IsSpecial(ph) ? Null : in[i] * ph);
        }
    }

    return;
}

/**
 * @brief Apply Hillier photometric correction
 *
 * Short function dispatched for each line to apply the Hillier photometrc
 * correction function.
 *
 * @author kbecker (2/20/2010)
 *
 * @param in Buffer containing input data
 * @param out Buffer of photometrically corrected data
 */
void phoCalWithBackplane ( std::vector<Isis::Buffer *> &in, std::vector<Isis::Buffer *> &out ) {

    Buffer &image = *in[0];
    Buffer &phase = *in[1];
    Buffer &emission = *in[2];
    Buffer &incidence = *in[3];
    Buffer &calibrated = *out[0];

    for (int i = 0; i < image.size(); i++) {
        //  Don't correct special pixels
        if (IsSpecial(image[i])) {
            calibrated[i] = image[i];
        }
        else {
            // Get correction and test for validity
            double ph = pho->photometry(incidence[i], emission[i], phase[i], image.Band(i));
            calibrated[i] = (IsSpecial(ph) ? Null : image[i] * ph);
        }
    }

    return;
}
