#!/usr/bin/python

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "1. Tab to the <button> button",
    ["BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button'",
     "     VISIBLE:  '<button> push button <input type', cursor=1",
     "BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button'",
     "     VISIBLE:  '<button> push button <input type', cursor=1",
     "SPEECH OUTPUT: '<button> push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(utils.AssertPresentationAction(
    "2. Basic Where Am I on <button>",
    ["BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button'",
     "     VISIBLE:  '<button> push button <input type', cursor=1",
     "SPEECH OUTPUT: '<button>'",
     "SPEECH OUTPUT: 'push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "3. Tab to <input type='button'>",
    ["BRAILLE LINE:  '<button> push button  Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button <input type='button'> push button'",
     "     VISIBLE:  '<input type='button'> push butto', cursor=1",
     "BRAILLE LINE:  '<button> push button  Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button <input type='button'> push button'",
     "     VISIBLE:  '<input type='button'> push butto', cursor=1",
     "SPEECH OUTPUT: '<input type='button'> push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(utils.AssertPresentationAction(
    "4. Basic Where Am I on <input type='button'>",
    ["BRAILLE LINE:  '<button> push button  Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button <input type='button'> push button'",
     "     VISIBLE:  '<input type='button'> push butto', cursor=1",
     "SPEECH OUTPUT: '<input type='button'>'",
     "SPEECH OUTPUT: 'push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "5. Tab to first Create button",
    ["BRAILLE LINE:  '<button> push button  Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button <input type='button'> push button'",
     "     VISIBLE:  'Create push button Create push b', cursor=1",
     "BRAILLE LINE:  '<button> push button  Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button <input type='button'> push button'",
     "     VISIBLE:  'Create push button Create push b', cursor=1",
     "SPEECH OUTPUT: 'Create push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(utils.AssertPresentationAction(
    "6. Basic Where Am I on first Create button",
    ["BRAILLE LINE:  '<button> push button  Create push button Create push button Viewpush button Createsave options push button   Savesave options push button Disabled push button push button <input type='button'> push button'",
     "     VISIBLE:  'Create push button Create push b', cursor=1",
     "SPEECH OUTPUT: 'Create'",
     "SPEECH OUTPUT: 'push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "7. Tab to View push button",
    ["BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button push button Createsave options push button   Savesave options push button Disabled push button push button View'",
     "     VISIBLE:  '<button> push button <input type', cursor=0",
     "BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button push button Createsave options push button   Savesave options push button Disabled push button push button View'",
     "     VISIBLE:  '<button> push button <input type', cursor=0",
     "SPEECH OUTPUT: 'View push button view title'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "8. Tab to second Create button",
    ["BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button save options push button   Savesave options push button Disabled push button push button Create'",
     "     VISIBLE:  '<button> push button <input type', cursor=0",
     "BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button save options push button   Savesave options push button Disabled push button push button Create'",
     "     VISIBLE:  '<button> push button <input type', cursor=0",
     "SPEECH OUTPUT: 'Create push button creative title'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "9. Tab to drop down menu on Create -- whose tooltip and accessible name is 'save options'",
    ["BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button    Savesave options push button Disabled push button push button Createsave options push button'",
     "     VISIBLE:  'save options push button', cursor=1",
     "BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button    Savesave options push button Disabled push button push button Createsave options push button'",
     "     VISIBLE:  'save options push button', cursor=1",
     "SPEECH OUTPUT: 'save options push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(TypeAction(" "))
sequence.append(utils.AssertPresentationAction(
    "10. Open drop down menu on Create",
    ["BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button    Savesave options push button Disabled push button push button Createsave options push button'",
     "     VISIBLE:  'save options push button', cursor=1",
     "BRAILLE LINE:  'Create blank'",
     "     VISIBLE:  'Create blank', cursor=1",
     "BRAILLE LINE:  'Focus mode'",
     "     VISIBLE:  'Focus mode', cursor=0",
     "BRAILLE LINE:  'Create blank'",
     "     VISIBLE:  'Create blank', cursor=1",
     "SPEECH OUTPUT: 'createMenu panel'",
     "SPEECH OUTPUT: 'Create blank'",
     "SPEECH OUTPUT: 'Focus mode' voice=system"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "11. Down to Create from template",
    ["BRAILLE LINE:  'Create from template'",
     "     VISIBLE:  'Create from template', cursor=1",
     "BRAILLE LINE:  'Create from template'",
     "     VISIBLE:  'Create from template', cursor=1",
     "SPEECH OUTPUT: 'Create from template'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Escape"))
sequence.append(utils.AssertPresentationAction(
    "12. Close Create drop down menu",
    ["BRAILLE LINE:  'save options collapsed push button'",
     "     VISIBLE:  'save options collapsed push butt', cursor=1",
     "BRAILLE LINE:  'save options collapsed push button'",
     "     VISIBLE:  'save options collapsed push butt', cursor=1",
     "SPEECH OUTPUT: 'save options collapsed push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "13. Go to Edit!",
    ["BRAILLE LINE:  'Edit! push button'",
     "     VISIBLE:  'Edit! push button', cursor=1",
     "BRAILLE LINE:  'Browse mode'",
     "     VISIBLE:  'Browse mode', cursor=0",
     "BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button Create   Savesave options push button Disabled push button push button Edit!Edit! push button'",
     "     VISIBLE:  'Edit! push button', cursor=1",
     "SPEECH OUTPUT: 'Edit! push button edit title'",
     "SPEECH OUTPUT: 'Browse mode' voice=system"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("space"))
sequence.append(utils.AssertPresentationAction(
    "14. Open the Edit! menu",
    ["BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button Create   Savesave options push button Disabled push button push button Edit!Edit! push button'",
     "     VISIBLE:  'Edit! push button', cursor=1",
     "BRAILLE LINE:  'Cut'",
     "     VISIBLE:  'Cut', cursor=1",
     "BRAILLE LINE:  'Focus mode'",
     "     VISIBLE:  'Focus mode', cursor=0",
     "BRAILLE LINE:  'Cut'",
     "     VISIBLE:  'Cut', cursor=1",
     "SPEECH OUTPUT: 'Edit! edit title panel'",
     "SPEECH OUTPUT: 'Edit! Edit! edit title menu'",
     "SPEECH OUTPUT: 'Cut'",
     "SPEECH OUTPUT: 'Focus mode' voice=system"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "15. Go to Copy",
    ["BRAILLE LINE:  'Copy'",
     "     VISIBLE:  'Copy', cursor=1",
     "BRAILLE LINE:  'Copy'",
     "     VISIBLE:  'Copy', cursor=1",
     "SPEECH OUTPUT: 'Copy'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "16. Go to Paste",
    ["BRAILLE LINE:  'Paste'",
     "     VISIBLE:  'Paste', cursor=1",
     "BRAILLE LINE:  'Paste'",
     "     VISIBLE:  'Paste', cursor=1",
     "SPEECH OUTPUT: 'Paste'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "17. Go to Submenu",
    ["BRAILLE LINE:  'Submenu menu'",
     "     VISIBLE:  'Submenu menu', cursor=1",
     "BRAILLE LINE:  'Submenu menu'",
     "     VISIBLE:  'Submenu menu', cursor=1",
     "SPEECH OUTPUT: 'Submenu menu'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("space"))
sequence.append(utils.AssertPresentationAction(
    "18. Open Submenu",
    ["BRAILLE LINE:  'Submenu Item One'",
     "     VISIBLE:  'Submenu Item One', cursor=1",
     "BRAILLE LINE:  'Submenu Item One'",
     "     VISIBLE:  'Submenu Item One', cursor=1",
     "SPEECH OUTPUT: 'Submenu panel'",
     "SPEECH OUTPUT: 'Submenu menu'",
     "SPEECH OUTPUT: 'Submenu Item One'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "19. Down to Submenu Item Two",
    ["BRAILLE LINE:  'Submenu Item Two'",
     "     VISIBLE:  'Submenu Item Two', cursor=1",
     "BRAILLE LINE:  'Submenu Item Two'",
     "     VISIBLE:  'Submenu Item Two', cursor=1",
     "SPEECH OUTPUT: 'Submenu Item Two'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Down"))
sequence.append(utils.AssertPresentationAction(
    "20. Down to Deeper Submenu",
    ["BRAILLE LINE:  'Deeper Submenu menu'",
     "     VISIBLE:  'Deeper Submenu menu', cursor=1",
     "BRAILLE LINE:  'Deeper Submenu menu'",
     "     VISIBLE:  'Deeper Submenu menu', cursor=1",
     "SPEECH OUTPUT: 'Deeper Submenu menu'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Escape"))
sequence.append(utils.AssertPresentationAction(
    "21. Close the Submenu",
    ["KNOWN ISSUE: Too much speech context",
     "BRAILLE LINE:  'Submenu menu'",
     "     VISIBLE:  'Submenu menu', cursor=1",
     "BRAILLE LINE:  'Submenu menu'",
     "     VISIBLE:  'Submenu menu', cursor=1",
     "SPEECH OUTPUT: 'Edit! edit title panel'",
     "SPEECH OUTPUT: 'Edit! Edit! edit title menu'",
     "SPEECH OUTPUT: 'Submenu menu'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Escape"))
sequence.append(utils.AssertPresentationAction(
    "22. Close the Edit! menu",
    ["BRAILLE LINE:  'Edit! collapsed push button'",
     "     VISIBLE:  'Edit! collapsed push button', cursor=1",
     "BRAILLE LINE:  'Edit! collapsed push button'",
     "     VISIBLE:  'Edit! collapsed push button', cursor=1",
     "SPEECH OUTPUT: 'Edit! collapsed push button edit title'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "23. Tab to the Color button",
    ["BRAILLE LINE:  'Color push button'",
     "     VISIBLE:  'Color push button', cursor=1",
     "BRAILLE LINE:  'Browse mode'",
     "     VISIBLE:  'Browse mode', cursor=0",
     "BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button Create   Savesave options push button Disabled push button push button ColorColor push button'",
     "     VISIBLE:  'Color push button', cursor=1",
     "SPEECH OUTPUT: 'Color push button'",
     "SPEECH OUTPUT: 'Browse mode' voice=system"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("space"))
sequence.append(utils.AssertPresentationAction(
    "24. Open the Color menu",
    ["KNOWN ISSUE: This is messed up on several different levels",
     "BRAILLE LINE:  '<button> push button <input type='button'> push button Create push button Create push button Viewpush button Create   Savesave options push button Disabled push button push button ColorColor push button'",
     "     VISIBLE:  'Color push button', cursor=1",
     "BRAILLE LINE:  'white lime green blue'",
     "     VISIBLE:  'white lime green blue', cursor=0",
     "BRAILLE LINE:  'Focus mode'",
     "     VISIBLE:  'Focus mode', cursor=0",
     "BRAILLE LINE:  'white table cell'",
     "     VISIBLE:  'white table cell', cursor=1",
     "BRAILLE LINE:  '\ufffc $l'",
     "     VISIBLE:  '\ufffc $l', cursor=2",
     "SPEECH OUTPUT: 'Color panel'",
     "SPEECH OUTPUT: 'white'",
     "SPEECH OUTPUT: 'Focus mode' voice=system"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Right"))
sequence.append(utils.AssertPresentationAction(
    "25. Go to lime",
    ["KNOWN ISSUE: We should not be presenting this embedded object char",
     "BRAILLE LINE:  'lime table cell'",
     "     VISIBLE:  'lime table cell', cursor=1",
     "BRAILLE LINE:  'lime table cell'",
     "     VISIBLE:  'lime table cell', cursor=1",
     "BRAILLE LINE:  '\ufffc $l'",
     "     VISIBLE:  '\ufffc $l', cursor=2",
     "SPEECH OUTPUT: 'lime'",
     "SPEECH OUTPUT: '\ufffc'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Escape"))
sequence.append(utils.AssertPresentationAction(
    "26. Close the Color menu",
    ["BRAILLE LINE:  'Color collapsed push button'",
     "     VISIBLE:  'Color collapsed push button', cursor=1",
     "BRAILLE LINE:  'Color collapsed push button'",
     "     VISIBLE:  'Color collapsed push button', cursor=1",
     "SPEECH OUTPUT: 'Color collapsed push button'"]))

for i in range(18):
    sequence.append(KeyComboAction("Tab"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "27. Tab to the toggle me off button",
    ["BRAILLE LINE:  'Toggle me off&=y Toggle me off toggle button'",
     "     VISIBLE:  '&=y Toggle me off toggle button', cursor=1",
     "BRAILLE LINE:  'Toggle me off&=y Toggle me off toggle button'",
     "     VISIBLE:  '&=y Toggle me off toggle button', cursor=1",
     "SPEECH OUTPUT: 'Toggle me off toggle button pressed'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("space"))
sequence.append(utils.AssertPresentationAction(
    "28. Toggle the state of the toggle me off button",
    ["BRAILLE LINE:  'Toggle me off& y toggle me on Toggle me off toggle button'",
     "     VISIBLE:  '& y toggle me on Toggle me off t', cursor=1",
     "BRAILLE LINE:  'toggle me on& y toggle me on Toggle me off toggle button'",
     "     VISIBLE:  '& y toggle me on Toggle me off t', cursor=1",
     "BRAILLE LINE:  'toggle me on& y toggle me on Toggle me off toggle button'",
     "     VISIBLE:  '& y toggle me on Toggle me off t', cursor=1",
     "SPEECH OUTPUT: 'not pressed'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("space"))
sequence.append(utils.AssertPresentationAction(
    "29. Toggle the state of the toggle me off button",
    ["BRAILLE LINE:  'toggle me on&=y toggle me off Toggle me off toggle button'",
     "     VISIBLE:  '&=y toggle me off Toggle me off ', cursor=1",
     "BRAILLE LINE:  'toggle me off&=y toggle me off Toggle me off toggle button'",
     "     VISIBLE:  '&=y toggle me off Toggle me off ', cursor=1",
     "BRAILLE LINE:  'toggle me off&=y toggle me off Toggle me off toggle button'",
     "     VISIBLE:  '&=y toggle me off Toggle me off ', cursor=1",
     "SPEECH OUTPUT: 'pressed'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("Tab"))
sequence.append(utils.AssertPresentationAction(
    "30. Tab to the toggle me button",
    ["BRAILLE LINE:  'toggle me off&=y toggle me off Toggle me off toggle button push button push button Toggle meToggle me push button'",
     "     VISIBLE:  'Toggle me push button', cursor=1",
     "BRAILLE LINE:  'toggle me off&=y toggle me off Toggle me off toggle button push button push button Toggle meToggle me push button'",
     "     VISIBLE:  'Toggle me push button', cursor=1",
     "SPEECH OUTPUT: 'Toggle me push button'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("space"))
sequence.append(utils.AssertPresentationAction(
    "31. Toggle the state of the toggle me button",
    ["KNOWN ISSUE: We seem to be missing the expected events and state changes. Dojo bug?",
     "BRAILLE LINE:  'toggle me off&=y toggle me off Toggle me off toggle button push button push button Toggle meToggle me push button'",
     "     VISIBLE:  'Toggle me push button', cursor=1"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("space"))
sequence.append(utils.AssertPresentationAction(
    "32. Toggle the state of the toggle me button",
    ["KNOWN ISSUE: We seem to be missing the expected events and state changes. Dojo bug?",
     "BRAILLE LINE:  'toggle me off&=y toggle me off Toggle me off toggle button push button push button Toggle meToggle me push button'",
     "     VISIBLE:  'Toggle me push button', cursor=1"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()