Activities/ReckonPrimer.tests/README.txt
WN091114

legend: the prompt is >

run all tests:
~~~~~~~~~~~~~~
ReckonPrimer.tests> python _all_test.py

... must finish with
##### ReckonPrimer.tests/_all-test.py SUCCESS ########################
##################################### ^^^^^^^ ########################

setup test-driven development: 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
all directories involved need to be in the PYTHONPATH:

> echo $PYTHONPATH

# PYTHONPATH=$PYTHONPATH:
# /home/neuper/Activities/ReckonPrimer.activity:
# /home/neuper/Activities/ReckonPrimer.tests:
# /home/neuper/Activities/ReckonPrimer.tests/ReckonPrimerActivity:
# /home/neuper/Activities/ReckonPrimer.tests/addsubsimp:
# /home/neuper/Activities/ReckonPrimer.tests/author:
# /home/neuper/Activities/ReckonPrimer.tests/coach:
# /home/neuper/Activities/ReckonPrimer.tests/collection:
# /home/neuper/Activities/ReckonPrimer.tests/display:
# /home/neuper/Activities/ReckonPrimer.tests/exercise:
# /home/neuper/Activities/ReckonPrimer.tests/learner:
# /home/neuper/Activities/ReckonPrimer.tests/passten:
# /home/neuper/Activities/ReckonPrimer.tests/session:
# /home/neuper/Activities/ReckonPrimer.tests/timer:
# /home/neuper/Activities/ReckonPrimer.tests/timesdiv:
# which is ....

> PYTHONPATH=$PYTHONPATH:/home/neuper/Activities/ReckonPrimer.activity:/home/neuper/Activities/ReckonPrimer.tests:/home/neuper/Activities/ReckonPrimer.tests/ReckonPrimerActivity:/home/neuper/Activities/ReckonPrimer.tests/addsubsimp:/home/neuper/Activities/ReckonPrimer.tests/author:/home/neuper/Activities/ReckonPrimer.tests/coach:/home/neuper/Activities/ReckonPrimer.tests/collection:/home/neuper/Activities/ReckonPrimer.tests/display:/home/neuper/Activities/ReckonPrimer.tests/exercise:/home/neuper/Activities/ReckonPrimer.tests/learner:/home/neuper/Activities/ReckonPrimer.tests/passten:/home/neuper/Activities/ReckonPrimer.tests/session:/home/neuper/Activities/ReckonPrimer.tests/timer:/home/neuper/Activities/ReckonPrimer.tests/timesdiv

> export PYTHONPATH

... these commands are required at the beginning of each session, unless ...

organization of test-driven development:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# each module of the production code contains one class
# for each module there is a directory containing all related tests
# in each directory RP.tests/dirname there is a file _dirname_test.py
# this _dirname_test.py contains "def _dirname_test():" which executes all 
  tests in this directory
# test modules are named module_name_test.py
# all test classes are named MockClassName
# all test methods are named test_method_name
