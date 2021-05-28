#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on May 28, 2021, at 16:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'EventTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Luke\\Documents\\GitHub\\Event-Task\\EventTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "standardizingRTs"
standardizingRTsClock = core.Clock()
std_instructions = visual.TextStim(win=win, name='std_instructions',
    text='For the next task, you will press:\n“C” for YES\n“N” for NO\n\nWe will practice this a few times before continuing.\n\nPress the space bar when you are ready.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue1 = keyboard.Keyboard()

# Initialize components for Routine "stdRT_loop"
stdRT_loopClock = core.Clock()
key_resp_stdRT = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
task_instructions = visual.TextStim(win=win, name='task_instructions',
    text='Welcome to the Event Task!\n\nYou will see a series of pictures. For each picture, you will answer the question: \nIs this something that might normally happen?\n\nUse your keyboard to respond. \nHit ‘C’ if the answer is YES.\nHit ‘N’ if the answer is NO.\n\nWe will start with a series of practice items. \n\nPress the space bar when you are ready.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue2 = keyboard.Keyboard()

# Initialize components for Routine "header_practice"
header_practiceClock = core.Clock()
practice_block = visual.TextStim(win=win, name='practice_block',
    text='Practice Block',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue3 = keyboard.Keyboard()

# Initialize components for Routine "practice"
practiceClock = core.Clock()
trial_instructions_practice = visual.TextStim(win=win, name='trial_instructions_practice',
    text='C = “YES”             N = “NO”',
    font='Open Sans',
    units='pix', pos=(0,-300), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_practice = keyboard.Keyboard()
image_practice = visual.ImageStim(
    win=win,
    name='image_practice', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "header_experiment"
header_experimentClock = core.Clock()
experiment_block = visual.TextStim(win=win, name='experiment_block',
    text='Experiment Block',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue4 = keyboard.Keyboard()

# Initialize components for Routine "experiment"
experimentClock = core.Clock()
trial_instructions = visual.TextStim(win=win, name='trial_instructions',
    text='C = “YES”             N = “NO”',
    font='Open Sans',
    units='pix', pos=(0,-300), height=30.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
breaktime=0

# Initialize components for Routine "breakblock"
breakblockClock = core.Clock()
breakimg = visual.ImageStim(
    win=win,
    name='breakimg', 
    image='breakfile.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
continue6 = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='This is the end of the Event Task.\n\nThank you!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
continue5 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "standardizingRTs"-------
continueRoutine = True
# update component parameters for each repeat
continue1.keys = []
continue1.rt = []
_continue1_allKeys = []
# keep track of which components have finished
standardizingRTsComponents = [std_instructions, continue1]
for thisComponent in standardizingRTsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
standardizingRTsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "standardizingRTs"-------
while continueRoutine:
    # get current time
    t = standardizingRTsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=standardizingRTsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *std_instructions* updates
    if std_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        std_instructions.frameNStart = frameN  # exact frame index
        std_instructions.tStart = t  # local t and not account for scr refresh
        std_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(std_instructions, 'tStartRefresh')  # time at next scr refresh
        std_instructions.setAutoDraw(True)
    
    # *continue1* updates
    waitOnFlip = False
    if continue1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue1.frameNStart = frameN  # exact frame index
        continue1.tStart = t  # local t and not account for scr refresh
        continue1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue1, 'tStartRefresh')  # time at next scr refresh
        continue1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(continue1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(continue1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if continue1.status == STARTED and not waitOnFlip:
        theseKeys = continue1.getKeys(keyList=['space'], waitRelease=False)
        _continue1_allKeys.extend(theseKeys)
        if len(_continue1_allKeys):
            continue1.keys = _continue1_allKeys[-1].name  # just the last key pressed
            continue1.rt = _continue1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in standardizingRTsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "standardizingRTs"-------
for thisComponent in standardizingRTsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('std_instructions.started', std_instructions.tStartRefresh)
thisExp.addData('std_instructions.stopped', std_instructions.tStopRefresh)
# check responses
if continue1.keys in ['', [], None]:  # No response was made
    continue1.keys = None
thisExp.addData('continue1.keys',continue1.keys)
if continue1.keys != None:  # we had a response
    thisExp.addData('continue1.rt', continue1.rt)
thisExp.addData('continue1.started', continue1.tStartRefresh)
thisExp.addData('continue1.stopped', continue1.tStopRefresh)
thisExp.nextEntry()
# the Routine "standardizingRTs" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
stdRT_trials = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('standardizingRTs.csv'),
    seed=None, name='stdRT_trials')
thisExp.addLoop(stdRT_trials)  # add the loop to the experiment
thisStdRT_trial = stdRT_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStdRT_trial.rgb)
if thisStdRT_trial != None:
    for paramName in thisStdRT_trial:
        exec('{} = thisStdRT_trial[paramName]'.format(paramName))

for thisStdRT_trial in stdRT_trials:
    currentLoop = stdRT_trials
    # abbreviate parameter names if possible (e.g. rgb = thisStdRT_trial.rgb)
    if thisStdRT_trial != None:
        for paramName in thisStdRT_trial:
            exec('{} = thisStdRT_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "stdRT_loop"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_stdRT.keys = []
    key_resp_stdRT.rt = []
    _key_resp_stdRT_allKeys = []
    text.setText(stimulus)
    # keep track of which components have finished
    stdRT_loopComponents = [key_resp_stdRT, text]
    for thisComponent in stdRT_loopComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stdRT_loopClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stdRT_loop"-------
    while continueRoutine:
        # get current time
        t = stdRT_loopClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stdRT_loopClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_stdRT* updates
        waitOnFlip = False
        if key_resp_stdRT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_stdRT.frameNStart = frameN  # exact frame index
            key_resp_stdRT.tStart = t  # local t and not account for scr refresh
            key_resp_stdRT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_stdRT, 'tStartRefresh')  # time at next scr refresh
            key_resp_stdRT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_stdRT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_stdRT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_stdRT.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_stdRT.getKeys(keyList=['c', 'n'], waitRelease=False)
            _key_resp_stdRT_allKeys.extend(theseKeys)
            if len(_key_resp_stdRT_allKeys):
                key_resp_stdRT.keys = _key_resp_stdRT_allKeys[-1].name  # just the last key pressed
                key_resp_stdRT.rt = _key_resp_stdRT_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stdRT_loopComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stdRT_loop"-------
    for thisComponent in stdRT_loopComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_stdRT.keys in ['', [], None]:  # No response was made
        key_resp_stdRT.keys = None
    stdRT_trials.addData('key_resp_stdRT.keys',key_resp_stdRT.keys)
    if key_resp_stdRT.keys != None:  # we had a response
        stdRT_trials.addData('key_resp_stdRT.rt', key_resp_stdRT.rt)
    stdRT_trials.addData('key_resp_stdRT.started', key_resp_stdRT.tStartRefresh)
    stdRT_trials.addData('key_resp_stdRT.stopped', key_resp_stdRT.tStopRefresh)
    stdRT_trials.addData('text.started', text.tStartRefresh)
    stdRT_trials.addData('text.stopped', text.tStopRefresh)
    # the Routine "stdRT_loop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'stdRT_trials'


# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
continue2.keys = []
continue2.rt = []
_continue2_allKeys = []
# keep track of which components have finished
instructionsComponents = [task_instructions, continue2]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *task_instructions* updates
    if task_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        task_instructions.frameNStart = frameN  # exact frame index
        task_instructions.tStart = t  # local t and not account for scr refresh
        task_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(task_instructions, 'tStartRefresh')  # time at next scr refresh
        task_instructions.setAutoDraw(True)
    
    # *continue2* updates
    waitOnFlip = False
    if continue2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue2.frameNStart = frameN  # exact frame index
        continue2.tStart = t  # local t and not account for scr refresh
        continue2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue2, 'tStartRefresh')  # time at next scr refresh
        continue2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(continue2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(continue2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if continue2.status == STARTED and not waitOnFlip:
        theseKeys = continue2.getKeys(keyList=['space'], waitRelease=False)
        _continue2_allKeys.extend(theseKeys)
        if len(_continue2_allKeys):
            continue2.keys = _continue2_allKeys[-1].name  # just the last key pressed
            continue2.rt = _continue2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('task_instructions.started', task_instructions.tStartRefresh)
thisExp.addData('task_instructions.stopped', task_instructions.tStopRefresh)
# check responses
if continue2.keys in ['', [], None]:  # No response was made
    continue2.keys = None
thisExp.addData('continue2.keys',continue2.keys)
if continue2.keys != None:  # we had a response
    thisExp.addData('continue2.rt', continue2.rt)
thisExp.addData('continue2.started', continue2.tStartRefresh)
thisExp.addData('continue2.stopped', continue2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "header_practice"-------
continueRoutine = True
# update component parameters for each repeat
continue3.keys = []
continue3.rt = []
_continue3_allKeys = []
# keep track of which components have finished
header_practiceComponents = [practice_block, continue3]
for thisComponent in header_practiceComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
header_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "header_practice"-------
while continueRoutine:
    # get current time
    t = header_practiceClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=header_practiceClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_block* updates
    if practice_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_block.frameNStart = frameN  # exact frame index
        practice_block.tStart = t  # local t and not account for scr refresh
        practice_block.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_block, 'tStartRefresh')  # time at next scr refresh
        practice_block.setAutoDraw(True)
    if practice_block.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice_block.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            practice_block.tStop = t  # not accounting for scr refresh
            practice_block.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_block, 'tStopRefresh')  # time at next scr refresh
            practice_block.setAutoDraw(False)
    
    # *continue3* updates
    waitOnFlip = False
    if continue3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue3.frameNStart = frameN  # exact frame index
        continue3.tStart = t  # local t and not account for scr refresh
        continue3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue3, 'tStartRefresh')  # time at next scr refresh
        continue3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(continue3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(continue3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if continue3.status == STARTED and not waitOnFlip:
        theseKeys = continue3.getKeys(keyList=['space'], waitRelease=False)
        _continue3_allKeys.extend(theseKeys)
        if len(_continue3_allKeys):
            continue3.keys = _continue3_allKeys[-1].name  # just the last key pressed
            continue3.rt = _continue3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in header_practiceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "header_practice"-------
for thisComponent in header_practiceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice_block.started', practice_block.tStartRefresh)
thisExp.addData('practice_block.stopped', practice_block.tStopRefresh)
# check responses
if continue3.keys in ['', [], None]:  # No response was made
    continue3.keys = None
thisExp.addData('continue3.keys',continue3.keys)
if continue3.keys != None:  # we had a response
    thisExp.addData('continue3.rt', continue3.rt)
thisExp.addData('continue3.started', continue3.tStartRefresh)
thisExp.addData('continue3.stopped', continue3.tStopRefresh)
thisExp.nextEntry()
# the Routine "header_practice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.csv'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_practice.keys = []
    key_resp_practice.rt = []
    _key_resp_practice_allKeys = []
    image_practice.setImage(file)
    # keep track of which components have finished
    practiceComponents = [trial_instructions_practice, key_resp_practice, image_practice]
    for thisComponent in practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_instructions_practice* updates
        if trial_instructions_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_instructions_practice.frameNStart = frameN  # exact frame index
            trial_instructions_practice.tStart = t  # local t and not account for scr refresh
            trial_instructions_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_instructions_practice, 'tStartRefresh')  # time at next scr refresh
            trial_instructions_practice.setAutoDraw(True)
        
        # *key_resp_practice* updates
        waitOnFlip = False
        if key_resp_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_practice.frameNStart = frameN  # exact frame index
            key_resp_practice.tStart = t  # local t and not account for scr refresh
            key_resp_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_practice, 'tStartRefresh')  # time at next scr refresh
            key_resp_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_practice.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_practice.getKeys(keyList=['c', 'n'], waitRelease=False)
            _key_resp_practice_allKeys.extend(theseKeys)
            if len(_key_resp_practice_allKeys):
                key_resp_practice.keys = _key_resp_practice_allKeys[-1].name  # just the last key pressed
                key_resp_practice.rt = _key_resp_practice_allKeys[-1].rt
                # was this correct?
                if (key_resp_practice.keys == str(corrAns)) or (key_resp_practice.keys == corrAns):
                    key_resp_practice.corr = 1
                else:
                    key_resp_practice.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image_practice* updates
        if image_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_practice.frameNStart = frameN  # exact frame index
            image_practice.tStart = t  # local t and not account for scr refresh
            image_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_practice, 'tStartRefresh')  # time at next scr refresh
            image_practice.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials.addData('trial_instructions_practice.started', trial_instructions_practice.tStartRefresh)
    practice_trials.addData('trial_instructions_practice.stopped', trial_instructions_practice.tStopRefresh)
    # check responses
    if key_resp_practice.keys in ['', [], None]:  # No response was made
        key_resp_practice.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_practice.corr = 1;  # correct non-response
        else:
           key_resp_practice.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('key_resp_practice.keys',key_resp_practice.keys)
    practice_trials.addData('key_resp_practice.corr', key_resp_practice.corr)
    if key_resp_practice.keys != None:  # we had a response
        practice_trials.addData('key_resp_practice.rt', key_resp_practice.rt)
    practice_trials.addData('key_resp_practice.started', key_resp_practice.tStartRefresh)
    practice_trials.addData('key_resp_practice.stopped', key_resp_practice.tStopRefresh)
    practice_trials.addData('image_practice.started', image_practice.tStartRefresh)
    practice_trials.addData('image_practice.stopped', image_practice.tStopRefresh)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice_trials'


# ------Prepare to start Routine "header_experiment"-------
continueRoutine = True
# update component parameters for each repeat
continue4.keys = []
continue4.rt = []
_continue4_allKeys = []
# keep track of which components have finished
header_experimentComponents = [experiment_block, continue4]
for thisComponent in header_experimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
header_experimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "header_experiment"-------
while continueRoutine:
    # get current time
    t = header_experimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=header_experimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *experiment_block* updates
    if experiment_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_block.frameNStart = frameN  # exact frame index
        experiment_block.tStart = t  # local t and not account for scr refresh
        experiment_block.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_block, 'tStartRefresh')  # time at next scr refresh
        experiment_block.setAutoDraw(True)
    if experiment_block.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > experiment_block.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            experiment_block.tStop = t  # not accounting for scr refresh
            experiment_block.frameNStop = frameN  # exact frame index
            win.timeOnFlip(experiment_block, 'tStopRefresh')  # time at next scr refresh
            experiment_block.setAutoDraw(False)
    
    # *continue4* updates
    waitOnFlip = False
    if continue4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue4.frameNStart = frameN  # exact frame index
        continue4.tStart = t  # local t and not account for scr refresh
        continue4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue4, 'tStartRefresh')  # time at next scr refresh
        continue4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(continue4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(continue4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if continue4.status == STARTED and not waitOnFlip:
        theseKeys = continue4.getKeys(keyList=['space'], waitRelease=False)
        _continue4_allKeys.extend(theseKeys)
        if len(_continue4_allKeys):
            continue4.keys = _continue4_allKeys[-1].name  # just the last key pressed
            continue4.rt = _continue4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in header_experimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "header_experiment"-------
for thisComponent in header_experimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('experiment_block.started', experiment_block.tStartRefresh)
thisExp.addData('experiment_block.stopped', experiment_block.tStopRefresh)
# check responses
if continue4.keys in ['', [], None]:  # No response was made
    continue4.keys = None
thisExp.addData('continue4.keys',continue4.keys)
if continue4.keys != None:  # we had a response
    thisExp.addData('continue4.rt', continue4.rt)
thisExp.addData('continue4.started', continue4.tStartRefresh)
thisExp.addData('continue4.stopped', continue4.tStopRefresh)
thisExp.nextEntry()
# the Routine "header_experiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
experiment_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experiment.csv'),
    seed=None, name='experiment_trials')
thisExp.addLoop(experiment_trials)  # add the loop to the experiment
thisExperiment_trial = experiment_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExperiment_trial.rgb)
if thisExperiment_trial != None:
    for paramName in thisExperiment_trial:
        exec('{} = thisExperiment_trial[paramName]'.format(paramName))

for thisExperiment_trial in experiment_trials:
    currentLoop = experiment_trials
    # abbreviate parameter names if possible (e.g. rgb = thisExperiment_trial.rgb)
    if thisExperiment_trial != None:
        for paramName in thisExperiment_trial:
            exec('{} = thisExperiment_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "experiment"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    image.setImage(file)
    if (experiment_trials.thisTrialN+1)%5==0:
        breaktime=1
    # keep track of which components have finished
    experimentComponents = [trial_instructions, key_resp, image]
    for thisComponent in experimentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    experimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "experiment"-------
    while continueRoutine:
        # get current time
        t = experimentClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=experimentClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_instructions* updates
        if trial_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trial_instructions.frameNStart = frameN  # exact frame index
            trial_instructions.tStart = t  # local t and not account for scr refresh
            trial_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_instructions, 'tStartRefresh')  # time at next scr refresh
            trial_instructions.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['c', 'n'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(corrAns)) or (key_resp.keys == corrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "experiment"-------
    for thisComponent in experimentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    experiment_trials.addData('trial_instructions.started', trial_instructions.tStartRefresh)
    experiment_trials.addData('trial_instructions.stopped', trial_instructions.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for experiment_trials (TrialHandler)
    experiment_trials.addData('key_resp.keys',key_resp.keys)
    experiment_trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        experiment_trials.addData('key_resp.rt', key_resp.rt)
    experiment_trials.addData('key_resp.started', key_resp.tStartRefresh)
    experiment_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    experiment_trials.addData('image.started', image.tStartRefresh)
    experiment_trials.addData('image.stopped', image.tStopRefresh)
    # the Routine "experiment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    breaktrials = data.TrialHandler(nReps=breaktime, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='breaktrials')
    thisExp.addLoop(breaktrials)  # add the loop to the experiment
    thisBreaktrial = breaktrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBreaktrial.rgb)
    if thisBreaktrial != None:
        for paramName in thisBreaktrial:
            exec('{} = thisBreaktrial[paramName]'.format(paramName))
    
    for thisBreaktrial in breaktrials:
        currentLoop = breaktrials
        # abbreviate parameter names if possible (e.g. rgb = thisBreaktrial.rgb)
        if thisBreaktrial != None:
            for paramName in thisBreaktrial:
                exec('{} = thisBreaktrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "breakblock"-------
        continueRoutine = True
        # update component parameters for each repeat
        continue6.keys = []
        continue6.rt = []
        _continue6_allKeys = []
        # keep track of which components have finished
        breakblockComponents = [breakimg, continue6]
        for thisComponent in breakblockComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        breakblockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "breakblock"-------
        while continueRoutine:
            # get current time
            t = breakblockClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=breakblockClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *breakimg* updates
            if breakimg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                breakimg.frameNStart = frameN  # exact frame index
                breakimg.tStart = t  # local t and not account for scr refresh
                breakimg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(breakimg, 'tStartRefresh')  # time at next scr refresh
                breakimg.setAutoDraw(True)
            
            # *continue6* updates
            waitOnFlip = False
            if continue6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                continue6.frameNStart = frameN  # exact frame index
                continue6.tStart = t  # local t and not account for scr refresh
                continue6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue6, 'tStartRefresh')  # time at next scr refresh
                continue6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(continue6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(continue6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if continue6.status == STARTED and not waitOnFlip:
                theseKeys = continue6.getKeys(keyList=['space'], waitRelease=False)
                _continue6_allKeys.extend(theseKeys)
                if len(_continue6_allKeys):
                    continue6.keys = _continue6_allKeys[-1].name  # just the last key pressed
                    continue6.rt = _continue6_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in breakblockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "breakblock"-------
        for thisComponent in breakblockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        breaktrials.addData('breakimg.started', breakimg.tStartRefresh)
        breaktrials.addData('breakimg.stopped', breakimg.tStopRefresh)
        # check responses
        if continue6.keys in ['', [], None]:  # No response was made
            continue6.keys = None
        breaktrials.addData('continue6.keys',continue6.keys)
        if continue6.keys != None:  # we had a response
            breaktrials.addData('continue6.rt', continue6.rt)
        breaktrials.addData('continue6.started', continue6.tStartRefresh)
        breaktrials.addData('continue6.stopped', continue6.tStopRefresh)
        breaktime=0
        # the Routine "breakblock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed breaktime repeats of 'breaktrials'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'experiment_trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
continue5.keys = []
continue5.rt = []
_continue5_allKeys = []
# keep track of which components have finished
endComponents = [end_text, continue5]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # *continue5* updates
    waitOnFlip = False
    if continue5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        continue5.frameNStart = frameN  # exact frame index
        continue5.tStart = t  # local t and not account for scr refresh
        continue5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(continue5, 'tStartRefresh')  # time at next scr refresh
        continue5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(continue5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(continue5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if continue5.status == STARTED and not waitOnFlip:
        theseKeys = continue5.getKeys(keyList=['space'], waitRelease=False)
        _continue5_allKeys.extend(theseKeys)
        if len(_continue5_allKeys):
            continue5.keys = _continue5_allKeys[-1].name  # just the last key pressed
            continue5.rt = _continue5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)
# check responses
if continue5.keys in ['', [], None]:  # No response was made
    continue5.keys = None
thisExp.addData('continue5.keys',continue5.keys)
if continue5.keys != None:  # we had a response
    thisExp.addData('continue5.rt', continue5.rt)
thisExp.addData('continue5.started', continue5.tStartRefresh)
thisExp.addData('continue5.stopped', continue5.tStopRefresh)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
