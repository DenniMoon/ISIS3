#include "Isis.h"
#include "ProcessMosaic.h"
#include "ProcessByLine.h"
#include "SpecialPixel.h"

using namespace std;
using namespace Isis;

void CreateMosaic(Buffer &buf);

/**
 * Handmos Application- Allows to hand place an image on the
 * mosaic with input, mosaic and band priorities. Band priority allows the
 * user the option to place a pixel on the mosaic based on the pixel in the
 * chosen band. The band can be specified by band number or Keyword as it
 * appears in BandBin group of the PVL label. Also has the  ability to track the
 * origin by adding a band to mosaic at the time of creation. As input images
 * are placed on the mosaic, the are stored as records in the table "InputImages"
 * in the mosaic. Ability to copy HS, LS, NULL values from input onto the mosaic.
 *
 */
void IsisMain() {
  // See if we need to create the output file
  UserInterface &ui = Application::GetUserInterface();

  int ns, nl, nb;

  ProcessMosaic p;

  bool bTrack = ui.GetBoolean("TRACK");
  p.SetTrackFlag(bTrack);
  
  string inputFile = ui.GetAsString("FROM");
  string mosaicFile = ui.GetFilename("MOSAIC");

  // Set up the mosaic priority, either the input cube will be
  // placed ontop of the mosaic or beneath it  
  ProcessMosaic::MosaicPriority priority;
  string sPriority = ui.GetString("PRIORITY");
  string sType;
  if(sPriority == "BENEATH") {
    priority = ProcessMosaic::mosaic;
  }
  else if(sPriority == "ONTOP") {
    priority = ProcessMosaic::input;
  }
  else if(sPriority == "AVERAGE") {
    priority = ProcessMosaic::average;
  }
  else {
    priority = ProcessMosaic::band;
    sType = ui.GetString("TYPE");
    if(sType == "BANDNUMBER") {
      p.SetBandNumber(ui.GetInteger("NUMBER"));
    }
    else {
      //keyname & key value
      p.SetBandKeyWord(ui.GetString("KEYNAME"), ui.GetString("KEYVALUE"));
    }
    // Band Criteria
    BandCriteria eCriteria = Lesser;
    if(ui.GetString("CRITERIA") == "GREATER")
      eCriteria = Greater;
    p.SetBandCriteria(eCriteria);
  }

  //set priority
  p.SetPriority(priority);
  
  if(ui.GetString("CREATE") == "YES") {
    ns = ui.GetInteger("NSAMPLES");
    nl = ui.GetInteger("NLINES");
    nb = ui.GetInteger("NBANDS");

    // Create the origin band if the Track Flag is set
    if(bTrack) {
      nb += 1;
    }
    else if(priority == ProcessMosaic::average) {
      nb *= 2;
    }
    p.SetCreateFlag(true);

    ProcessByLine bl;

    bl.Progress()->SetText("Initializing base mosaic");
    CubeAttributeInput iAtt(inputFile);
    bl.SetInputCube(inputFile, iAtt);

    if(!ui.GetBoolean("Propagate")) {
      bl.PropagateHistory(false);
      bl.PropagateLabels(false);
      bl.PropagateTables(false);
      bl.PropagatePolygons(false);
      bl.PropagateOriginalLabel(false);
    }

    CubeAttributeOutput oAtt = ui.GetOutputAttribute("MOSAIC");
    bl.SetOutputCube(mosaicFile, oAtt, ns, nl, nb);
    bl.ClearInputCubes();
    
    // Initialize the mosaic to defaults
    bl.StartProcess(CreateMosaic);
    bl.EndProcess();
  }

  // Set the input cube for the process object
  p.SetBandBinMatch(ui.GetBoolean("MATCHBANDBIN"));
  p.Progress()->SetText("Mosaicking");

  // Get the MatchDEM Flag
  p.SetMatchDEM(ui.GetBoolean("MATCHDEM"));
  
  // Get the value for HS, LS, NULL flags whether to transfer the special pixels
  // onto the mosaic. Holds good for "ontop" and "band" priorities only
  if(priority == ProcessMosaic::input || priority == ProcessMosaic::band || priority == ProcessMosaic::average) {
    p.SetHighSaturationFlag(ui.GetBoolean("HIGHSATURATION"));
    p.SetLowSaturationFlag(ui.GetBoolean("LOWSATURATION"));
    p.SetNullFlag(ui.GetBoolean("NULL"));
  }

  // Get the starting line/sample/band to place the input cube
  int outSample = ui.GetInteger("OUTSAMPLE") - ui.GetInteger("INSAMPLE") + 1;
  int outLine   = ui.GetInteger("OUTLINE")   - ui.GetInteger("INLINE")   + 1;
  int outBand   = ui.GetInteger("OUTBAND")   - ui.GetInteger("INBAND")   + 1;

  // Set the input image and attributes
  CubeAttributeInput inAtt(inputFile);
  p.SetInputCube(inputFile, inAtt);

  // Set the output mosaic
  Cube *to = p.SetOutputCube("MOSAIC");

  p.WriteHistory(*to);

  // Place the input in the mosaic
  //p.StartProcess(outSample, outLine, outBand, priority);
  p.StartProcess(outSample, outLine, outBand);

  if(bTrack != p.GetTrackFlag()) {
    ui.Clear("TRACK");
    ui.PutBoolean("TRACK", p.GetTrackFlag());
  }
  p.EndProcess();

  // Log the changes to NBANDS and to TRACK if any
  PvlObject hist = Isis::iApp->History();
  Isis::iApp->Log(hist.FindGroup("UserParameters"));
  PvlGroup imgPosition("ImageLocation");
  int iStartLine   = p.GetInputStartLineInMosaic();
  int iStartSample = p.GetInputStartSampleInMosaic();
  imgPosition += PvlKeyword("File", ui.GetFilename("FROM"));
  imgPosition += PvlKeyword("StartSample", iStartSample);
  imgPosition += PvlKeyword("StartLine", iStartLine);
  Application::Log(imgPosition);
}

/**
 * Initialize the mosaic to defaults
 *
 * @author sprasad (10/14/2009)
 *
 * @param buf
 */
void CreateMosaic(Buffer &buf) {
  for(int i = 0; i < buf.size(); i++) {
    buf[i] = NULL8;
  }
}
