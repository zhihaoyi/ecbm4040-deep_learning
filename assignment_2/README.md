# Assignment 2  - distributed in Github Repo e4040-2022Fall-assign2
The assignment is distributed as several jupyter notebooks and a number of directories and subdirectories in utils.

# Detailed instructions how to submit this assignment/homework:
1. The assignment will be distributed as a github classroom assignment - as a special repository accessed through a link
2. A students copy of the assignment gets created automaticaly with a special name - students have to rename the repo per instructions below
3. The solution(s) to the assignment have to be submitted inside that repository as a set of "solved" Jupyter Notebooks, and several modified python files which reside in directories/subdirectories. This step is done by pushing all the files to the main branch. 
4. Three files/screenshots need to be uploaded into the directory "figures" which prove that the assignment has been done in the cloud


## (Re)naming of the student repository (TODO students) 
INSTRUCTIONS for naming the student's solution repository for assignments with one student:
* This step will require changing the repository name
* Students MUST use the following name for the repository with their solutions: e4040-2022Fall-assign2-UNI (the first part "e4040-2022Fall-assign2" will probably be inherited from the assignment, so only UNI needs to be added) 
* Initially, the system will give the repo a name which ends with a  student's Github userid. The student MUST change that name and replace it with the name requested in the point above
* Good Example: e4040-2022Fall-assign2-zz9999;   Bad example: e4040-2022Fall-assign2-e4040-2022Fall-assign2-zz9999.
* This change can be done from the "Settings" tab which is located on the repo page.

INSTRUCTIONS for naming the students' solution repository for assignments with more students, such as the final project. Students need to use a 4-letter groupID): 
* Template: e4040-2022Fall-Project-GroupID-UNI1-UNI2-UNI3. -> Example: e4040-2022Fall-Project-MEME-zz9999-aa9999-aa0000.


# Organization of this directory

TODO students: Run commands to create a directory tree, as described in previous assignments

```
.
├── Assignment2_intro.ipynb
├── README.md
├── requirements.txt
├── ...
```./
├── Assignment2-intro.ipynb
├── README.md
├── best_model
│   ├── assets
│   ├── keras_metadata.pb
│   ├── saved_model.pb
│   └── variables
│       ├── variables.data-00000-of-00001
│       └── variables.index
├── data
│   ├── cifar-10-batches-py
│   │   ├── batches.meta
│   │   ├── data_batch_1
│   │   ├── data_batch_2
│   │   ├── data_batch_3
│   │   ├── data_batch_4
│   │   ├── data_batch_5
│   │   ├── readme.html
│   │   └── test_batch
│   ├── cifar-10-python.tar.gz
│   ├── sign_mnist_test.csv
│   └── sign_mnist_train.csv
├── figures
│   ├── zy2523_gcp_work_example_screenshot_1.png
│   ├── zy2523_gcp_work_example_screenshot_2.png
│   └── zy2523_gcp_work_example_screenshot_3.png
├── logs
│   ├── fit
│   │   ├── 20221027-213956
│   │   │   └── train
│   │   │       └── events.out.tfevents.1666906797.ecbm4040-zy2523.2668.160.v2
│   │   ├── 20221027-220454
│   │   │   └── train
│   │   │       └── events.out.tfevents.1666908295.ecbm4040-zy2523.2668.479.v2
│   │   ├── 20221027-220540
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666908340.ecbm4040-zy2523.2668.852.v2
│   │   │   │   ├── events.out.tfevents.1666908341.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_05_41
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666908341.ecbm4040-zy2523.2668.1857.v2
│   │   ├── 20221027-221109
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666908669.ecbm4040-zy2523.2668.7867.v2
│   │   │   │   ├── events.out.tfevents.1666908670.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_11_10
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666908671.ecbm4040-zy2523.2668.8872.v2
│   │   ├── 20221027-221138
│   │   │   └── train
│   │   │       └── events.out.tfevents.1666908698.ecbm4040-zy2523.2668.14820.v2
│   │   ├── 20221027-221302
│   │   │   └── train
│   │   │       └── events.out.tfevents.1666908783.ecbm4040-zy2523.2668.15148.v2
│   │   ├── 20221027-221316
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666908796.ecbm4040-zy2523.2668.15520.v2
│   │   │   │   ├── events.out.tfevents.1666908797.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_13_17
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666908798.ecbm4040-zy2523.2668.16525.v2
│   │   ├── 20221027-221339
│   │   │   └── train
│   │   │       └── events.out.tfevents.1666908819.ecbm4040-zy2523.2668.22473.v2
│   │   ├── 20221027-221349
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666908829.ecbm4040-zy2523.2668.22845.v2
│   │   │   │   ├── events.out.tfevents.1666908830.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_13_50
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666908831.ecbm4040-zy2523.2668.23850.v2
│   │   ├── 20221027-221456
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666908897.ecbm4040-zy2523.2668.29860.v2
│   │   │   │   ├── events.out.tfevents.1666908897.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_14_57
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666908898.ecbm4040-zy2523.2668.30865.v2
│   │   ├── 20221027-221530
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666908930.ecbm4040-zy2523.2668.36866.v2
│   │   │   │   ├── events.out.tfevents.1666908931.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_15_31
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666908932.ecbm4040-zy2523.2668.37871.v2
│   │   ├── 20221027-221949
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909189.ecbm4040-zy2523.2668.43872.v2
│   │   │   │   ├── events.out.tfevents.1666909190.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_19_50
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909190.ecbm4040-zy2523.2668.44877.v2
│   │   ├── 20221027-222115
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909275.ecbm4040-zy2523.2668.50878.v2
│   │   │   │   ├── events.out.tfevents.1666909276.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_21_16
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909277.ecbm4040-zy2523.2668.51883.v2
│   │   ├── 20221027-222130
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909290.ecbm4040-zy2523.2668.57884.v2
│   │   │   │   ├── events.out.tfevents.1666909291.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_21_31
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909291.ecbm4040-zy2523.2668.58889.v2
│   │   ├── 20221027-222305
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909386.ecbm4040-zy2523.2668.64890.v2
│   │   │   │   ├── events.out.tfevents.1666909386.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_23_06
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909387.ecbm4040-zy2523.2668.65895.v2
│   │   ├── 20221027-222424
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909464.ecbm4040-zy2523.2668.71896.v2
│   │   │   │   ├── events.out.tfevents.1666909465.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_24_25
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909466.ecbm4040-zy2523.2668.72901.v2
│   │   ├── 20221027-222434
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909475.ecbm4040-zy2523.2668.78849.v2
│   │   │   │   ├── events.out.tfevents.1666909476.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_24_36
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909476.ecbm4040-zy2523.2668.80008.v2
│   │   ├── 20221027-222448
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909489.ecbm4040-zy2523.2668.86123.v2
│   │   │   │   ├── events.out.tfevents.1666909490.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_24_50
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909490.ecbm4040-zy2523.2668.87282.v2
│   │   ├── 20221027-222526
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909527.ecbm4040-zy2523.2668.93397.v2
│   │   │   │   ├── events.out.tfevents.1666909528.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_25_28
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909529.ecbm4040-zy2523.2668.94646.v2
│   │   ├── 20221027-222546
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909546.ecbm4040-zy2523.2668.100929.v2
│   │   │   │   ├── events.out.tfevents.1666909547.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_25_47
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909548.ecbm4040-zy2523.2668.102178.v2
│   │   ├── 20221027-222642
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909603.ecbm4040-zy2523.2668.108461.v2
│   │   │   │   ├── events.out.tfevents.1666909603.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_26_43
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909604.ecbm4040-zy2523.2668.109710.v2
│   │   ├── 20221027-222810
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909691.ecbm4040-zy2523.2668.115993.v2
│   │   │   │   ├── events.out.tfevents.1666909691.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_28_11
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909692.ecbm4040-zy2523.2668.117242.v2
│   │   ├── 20221027-222826
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909706.ecbm4040-zy2523.2668.123525.v2
│   │   │   │   ├── events.out.tfevents.1666909707.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_28_27
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909708.ecbm4040-zy2523.2668.124774.v2
│   │   ├── 20221027-223122
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909882.ecbm4040-zy2523.2668.131057.v2
│   │   │   │   ├── events.out.tfevents.1666909883.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_31_23
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909884.ecbm4040-zy2523.2668.132306.v2
│   │   ├── 20221027-223141
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909901.ecbm4040-zy2523.2668.138589.v2
│   │   │   │   ├── events.out.tfevents.1666909902.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_31_42
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909903.ecbm4040-zy2523.2668.139838.v2
│   │   ├── 20221027-223234
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666909955.ecbm4040-zy2523.2668.146121.v2
│   │   │   │   ├── events.out.tfevents.1666909955.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_32_35
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666909956.ecbm4040-zy2523.2668.147360.v2
│   │   ├── 20221027-223408
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910048.ecbm4040-zy2523.2668.153641.v2
│   │   │   │   ├── events.out.tfevents.1666910049.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_34_09
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910050.ecbm4040-zy2523.2668.154880.v2
│   │   ├── 20221027-223430
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910070.ecbm4040-zy2523.2668.161161.v2
│   │   │   │   ├── events.out.tfevents.1666910071.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_34_31
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910072.ecbm4040-zy2523.2668.162400.v2
│   │   ├── 20221027-223514
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910114.ecbm4040-zy2523.2668.168681.v2
│   │   │   │   ├── events.out.tfevents.1666910115.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_35_15
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910116.ecbm4040-zy2523.2668.169930.v2
│   │   ├── 20221027-223527
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910127.ecbm4040-zy2523.2668.176213.v2
│   │   │   │   ├── events.out.tfevents.1666910128.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_35_28
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910129.ecbm4040-zy2523.2668.177462.v2
│   │   ├── 20221027-223543
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910143.ecbm4040-zy2523.2668.183745.v2
│   │   │   │   ├── events.out.tfevents.1666910144.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_35_44
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910145.ecbm4040-zy2523.2668.184994.v2
│   │   ├── 20221027-223553
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910154.ecbm4040-zy2523.2668.191277.v2
│   │   │   │   ├── events.out.tfevents.1666910155.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_35_55
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910155.ecbm4040-zy2523.2668.192766.v2
│   │   ├── 20221027-223612
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910172.ecbm4040-zy2523.2668.199717.v2
│   │   │   │   ├── events.out.tfevents.1666910173.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_36_13
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910174.ecbm4040-zy2523.2668.200966.v2
│   │   ├── 20221027-223645
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910205.ecbm4040-zy2523.2668.207249.v2
│   │   │   │   ├── events.out.tfevents.1666910206.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_36_46
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910207.ecbm4040-zy2523.2668.208824.v2
│   │   ├── 20221027-223700
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910220.ecbm4040-zy2523.2668.215781.v2
│   │   │   │   ├── events.out.tfevents.1666910221.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_37_01
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910222.ecbm4040-zy2523.2668.217442.v2
│   │   ├── 20221027-223909
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910349.ecbm4040-zy2523.2668.224405.v2
│   │   │   │   ├── events.out.tfevents.1666910350.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_39_10
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910352.ecbm4040-zy2523.2668.226066.v2
│   │   ├── 20221027-224109
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910470.ecbm4040-zy2523.2668.233029.v2
│   │   │   │   ├── events.out.tfevents.1666910471.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_41_11
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910472.ecbm4040-zy2523.2668.234690.v2
│   │   ├── 20221027-224126
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910487.ecbm4040-zy2523.2668.241653.v2
│   │   │   │   ├── events.out.tfevents.1666910488.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_41_28
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910489.ecbm4040-zy2523.2668.243314.v2
│   │   ├── 20221027-224205
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910525.ecbm4040-zy2523.2668.250277.v2
│   │   │   │   ├── events.out.tfevents.1666910527.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_42_07
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910528.ecbm4040-zy2523.2668.251938.v2
│   │   ├── 20221027-224230
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910550.ecbm4040-zy2523.2668.258901.v2
│   │   │   │   ├── events.out.tfevents.1666910552.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_42_32
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910553.ecbm4040-zy2523.2668.260562.v2
│   │   ├── 20221027-224251
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910571.ecbm4040-zy2523.2668.267525.v2
│   │   │   │   ├── events.out.tfevents.1666910572.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_42_52
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910573.ecbm4040-zy2523.2668.269186.v2
│   │   ├── 20221027-224344
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910625.ecbm4040-zy2523.2668.276149.v2
│   │   │   │   ├── events.out.tfevents.1666910626.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_43_46
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910627.ecbm4040-zy2523.2668.277810.v2
│   │   ├── 20221027-224412
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910653.ecbm4040-zy2523.2668.284773.v2
│   │   │   │   ├── events.out.tfevents.1666910654.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_44_14
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910655.ecbm4040-zy2523.2668.286434.v2
│   │   ├── 20221027-224432
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910673.ecbm4040-zy2523.2668.293397.v2
│   │   │   │   ├── events.out.tfevents.1666910674.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_44_34
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910675.ecbm4040-zy2523.2668.295058.v2
│   │   ├── 20221027-224456
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910697.ecbm4040-zy2523.2668.302021.v2
│   │   │   │   ├── events.out.tfevents.1666910698.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_44_58
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910699.ecbm4040-zy2523.2668.303682.v2
│   │   ├── 20221027-224518
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910718.ecbm4040-zy2523.2668.310645.v2
│   │   │   │   ├── events.out.tfevents.1666910719.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_45_19
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910721.ecbm4040-zy2523.2668.312306.v2
│   │   ├── 20221027-224555
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910756.ecbm4040-zy2523.2668.319269.v2
│   │   │   │   ├── events.out.tfevents.1666910757.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_45_57
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910758.ecbm4040-zy2523.2668.320930.v2
│   │   ├── 20221027-224634
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910794.ecbm4040-zy2523.2668.327893.v2
│   │   │   │   ├── events.out.tfevents.1666910795.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_46_35
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910797.ecbm4040-zy2523.2668.329554.v2
│   │   ├── 20221027-224719
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910839.ecbm4040-zy2523.2668.336517.v2
│   │   │   │   ├── events.out.tfevents.1666910840.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_47_20
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910841.ecbm4040-zy2523.2668.338178.v2
│   │   ├── 20221027-224749
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910869.ecbm4040-zy2523.2668.345141.v2
│   │   │   │   ├── events.out.tfevents.1666910871.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_47_51
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910872.ecbm4040-zy2523.2668.346802.v2
│   │   ├── 20221027-224821
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910902.ecbm4040-zy2523.2668.353765.v2
│   │   │   │   ├── events.out.tfevents.1666910903.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_48_23
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910905.ecbm4040-zy2523.2668.355426.v2
│   │   ├── 20221027-224851
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910932.ecbm4040-zy2523.2668.362389.v2
│   │   │   │   ├── events.out.tfevents.1666910933.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_48_53
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910935.ecbm4040-zy2523.2668.364050.v2
│   │   ├── 20221027-224923
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910963.ecbm4040-zy2523.2668.371013.v2
│   │   │   │   ├── events.out.tfevents.1666910964.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_49_24
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910966.ecbm4040-zy2523.2668.372674.v2
│   │   ├── 20221027-224950
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666910990.ecbm4040-zy2523.2668.379637.v2
│   │   │   │   ├── events.out.tfevents.1666910992.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_49_52
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666910994.ecbm4040-zy2523.2668.381298.v2
│   │   ├── 20221027-225054
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911055.ecbm4040-zy2523.2668.388261.v2
│   │   │   │   ├── events.out.tfevents.1666911056.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_50_56
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911058.ecbm4040-zy2523.2668.389922.v2
│   │   ├── 20221027-225123
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911083.ecbm4040-zy2523.2668.396885.v2
│   │   │   │   ├── events.out.tfevents.1666911084.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_51_24
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911086.ecbm4040-zy2523.2668.398546.v2
│   │   ├── 20221027-225150
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911111.ecbm4040-zy2523.2668.405509.v2
│   │   │   │   ├── events.out.tfevents.1666911112.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_51_52
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911114.ecbm4040-zy2523.2668.407170.v2
│   │   ├── 20221027-225220
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911140.ecbm4040-zy2523.2668.414133.v2
│   │   │   │   ├── events.out.tfevents.1666911141.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_52_21
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911143.ecbm4040-zy2523.2668.415794.v2
│   │   ├── 20221027-225247
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911168.ecbm4040-zy2523.2668.422757.v2
│   │   │   │   ├── events.out.tfevents.1666911169.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_52_49
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911171.ecbm4040-zy2523.2668.424418.v2
│   │   ├── 20221027-225327
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911208.ecbm4040-zy2523.2668.431381.v2
│   │   │   │   ├── events.out.tfevents.1666911209.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_53_29
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911210.ecbm4040-zy2523.2668.433042.v2
│   │   ├── 20221027-225349
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911229.ecbm4040-zy2523.2668.440005.v2
│   │   │   │   ├── events.out.tfevents.1666911230.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_53_50
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911231.ecbm4040-zy2523.2668.441666.v2
│   │   ├── 20221027-225409
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911250.ecbm4040-zy2523.2668.448629.v2
│   │   │   │   ├── events.out.tfevents.1666911251.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_54_11
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911252.ecbm4040-zy2523.2668.450290.v2
│   │   ├── 20221027-225433
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911274.ecbm4040-zy2523.2668.457253.v2
│   │   │   │   ├── events.out.tfevents.1666911275.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_54_35
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911277.ecbm4040-zy2523.2668.458914.v2
│   │   ├── 20221027-225510
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911311.ecbm4040-zy2523.2668.465877.v2
│   │   │   │   ├── events.out.tfevents.1666911312.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_55_12
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911313.ecbm4040-zy2523.2668.467452.v2
│   │   ├── 20221027-225538
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911339.ecbm4040-zy2523.2668.474409.v2
│   │   │   │   ├── events.out.tfevents.1666911340.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_55_40
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911341.ecbm4040-zy2523.2668.475898.v2
│   │   ├── 20221027-225601
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911361.ecbm4040-zy2523.2668.482849.v2
│   │   │   │   ├── events.out.tfevents.1666911362.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_56_02
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911363.ecbm4040-zy2523.2668.484424.v2
│   │   ├── 20221027-225622
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911383.ecbm4040-zy2523.2668.491381.v2
│   │   │   │   ├── events.out.tfevents.1666911384.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_56_24
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911385.ecbm4040-zy2523.2668.492956.v2
│   │   ├── 20221027-225658
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911418.ecbm4040-zy2523.2668.499913.v2
│   │   │   │   ├── events.out.tfevents.1666911419.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_56_59
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911421.ecbm4040-zy2523.2668.501488.v2
│   │   ├── 20221027-225734
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911455.ecbm4040-zy2523.2668.508445.v2
│   │   │   │   ├── events.out.tfevents.1666911456.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_57_36
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911457.ecbm4040-zy2523.2668.510020.v2
│   │   ├── 20221027-225757
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911477.ecbm4040-zy2523.2668.516977.v2
│   │   │   │   ├── events.out.tfevents.1666911479.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_57_59
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911480.ecbm4040-zy2523.2668.518552.v2
│   │   ├── 20221027-225818
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911498.ecbm4040-zy2523.2668.525509.v2
│   │   │   │   ├── events.out.tfevents.1666911499.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_58_19
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911500.ecbm4040-zy2523.2668.527084.v2
│   │   ├── 20221027-225837
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911517.ecbm4040-zy2523.2668.534041.v2
│   │   │   │   ├── events.out.tfevents.1666911518.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_58_38
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911520.ecbm4040-zy2523.2668.535616.v2
│   │   ├── 20221027-225905
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911545.ecbm4040-zy2523.2668.542573.v2
│   │   │   │   ├── events.out.tfevents.1666911546.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_59_06
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911548.ecbm4040-zy2523.2668.544148.v2
│   │   ├── 20221027-225934
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911575.ecbm4040-zy2523.2668.551105.v2
│   │   │   │   ├── events.out.tfevents.1666911576.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_59_36
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911577.ecbm4040-zy2523.2668.552680.v2
│   │   ├── 20221027-225954
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911594.ecbm4040-zy2523.2668.559637.v2
│   │   │   │   ├── events.out.tfevents.1666911595.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_22_59_55
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911596.ecbm4040-zy2523.2668.561212.v2
│   │   ├── 20221027-230013
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911614.ecbm4040-zy2523.2668.568169.v2
│   │   │   │   ├── events.out.tfevents.1666911615.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_23_00_15
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911616.ecbm4040-zy2523.2668.569744.v2
│   │   ├── 20221027-230249
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666911770.ecbm4040-zy2523.5437.160.v2
│   │   │   │   ├── events.out.tfevents.1666911771.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_23_02_51
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666911773.ecbm4040-zy2523.5437.1736.v2
│   │   ├── 20221027-234459
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666914300.ecbm4040-zy2523.5676.160.v2
│   │   │   │   ├── events.out.tfevents.1666914301.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_23_45_01
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666914303.ecbm4040-zy2523.5676.1736.v2
│   │   ├── 20221027-235310
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666914791.ecbm4040-zy2523.5772.160.v2
│   │   │   │   ├── events.out.tfevents.1666914792.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_27_23_53_12
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666914793.ecbm4040-zy2523.5772.1736.v2
│   │   ├── 20221028-000042
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666915243.ecbm4040-zy2523.5872.160.v2
│   │   │   │   ├── events.out.tfevents.1666915244.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_28_00_00_44
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666915246.ecbm4040-zy2523.5872.1736.v2
│   │   ├── 20221028-000644
│   │   │   ├── train
│   │   │   │   ├── events.out.tfevents.1666915605.ecbm4040-zy2523.5996.160.v2
│   │   │   │   ├── events.out.tfevents.1666915606.ecbm4040-zy2523.profile-empty
│   │   │   │   └── plugins
│   │   │   │       └── profile
│   │   │   │           └── 2022_10_28_00_06_46
│   │   │   │               ├── ecbm4040-zy2523.input_pipeline.pb
│   │   │   │               ├── ecbm4040-zy2523.kernel_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.memory_profile.json.gz
│   │   │   │               ├── ecbm4040-zy2523.overview_page.pb
│   │   │   │               ├── ecbm4040-zy2523.tensorflow_stats.pb
│   │   │   │               ├── ecbm4040-zy2523.trace.json.gz
│   │   │   │               └── ecbm4040-zy2523.xplane.pb
│   │   │   └── validation
│   │   │       └── events.out.tfevents.1666915607.ecbm4040-zy2523.5996.1736.v2
│   │   ├── 20221029-193833
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667072314.ecbm4040-zy2523.2677.104.v2
│   │   ├── 20221030-010542
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667091943.ecbm4040-zy2523.4148.82.v2
│   │   ├── 20221030-011628
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667092588.ecbm4040-zy2523.4249.82.v2
│   │   ├── 20221030-013051
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667093452.ecbm4040-zy2523.4301.82.v2
│   │   ├── 20221030-013627
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667093788.ecbm4040-zy2523.4348.82.v2
│   │   ├── 20221030-014603
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667094364.ecbm4040-zy2523.4398.82.v2
│   │   ├── 20221030-015600
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667094960.ecbm4040-zy2523.4477.104.v2
│   │   ├── 20221030-020005
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667095206.ecbm4040-zy2523.4526.82.v2
│   │   ├── 20221030-021908
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667096349.ecbm4040-zy2523.4575.82.v2
│   │   ├── 20221030-023000
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667097000.ecbm4040-zy2523.4907.82.v2
│   │   ├── 20221030-023115
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667097075.ecbm4040-zy2523.4970.82.v2
│   │   ├── 20221030-023705
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667097425.ecbm4040-zy2523.5018.82.v2
│   │   ├── 20221030-024141
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667097702.ecbm4040-zy2523.5067.82.v2
│   │   ├── 20221030-025811
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667098692.ecbm4040-zy2523.5135.82.v2
│   │   ├── 20221030-033346
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667100827.ecbm4040-zy2523.5231.82.v2
│   │   ├── 20221030-033744
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667101064.ecbm4040-zy2523.5288.82.v2
│   │   ├── 20221030-034329
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667101410.ecbm4040-zy2523.5337.82.v2
│   │   ├── 20221030-034630
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667101591.ecbm4040-zy2523.5386.82.v2
│   │   ├── 20221030-034748
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667101668.ecbm4040-zy2523.5386.496.v2
│   │   ├── 20221030-040412
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667102652.ecbm4040-zy2523.2057.82.v2
│   │   ├── 20221030-200033
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667160034.ecbm4040-zy2523.2941.82.v2
│   │   ├── 20221030-200156
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667160117.ecbm4040-zy2523.2982.82.v2
│   │   ├── 20221030-211450
│   │   │   └── train
│   │   │       └── events.out.tfevents.1667164491.ecbm4040-zy2523.3212.82.v2
│   │   └── 20221031-010726
│   │       └── train
│   │           └── events.out.tfevents.1667178447.ecbm4040-zy2523.3627.82.v2
│   └── gradient_tape
│       └── 20221029-021935
│           ├── test
│           │   └── events.out.tfevents.1667009975.ecbm4040-zy2523.3220.87.v2
│           └── train
│               └── events.out.tfevents.1667009975.ecbm4040-zy2523.3220.79.v2
├── model
│   └── task3_model
│       ├── assets
│       ├── saved_model.pb
│       └── variables
│           ├── variables.data-00000-of-00001
│           └── variables.index
├── modified_prediction_labels_template.csv
├── predicted.csv
├── requirements.txt
├── task1-optimization.ipynb
├── task2-regularization.ipynb
├── task3_cnn.ipynb
├── task4-augmentation.ipynb
├── task5-kaggle.ipynb
└── utils
    ├── __pycache__
    │   ├── cifar_utils.cpython-36.pyc
    │   ├── image_generator.cpython-36.pyc
    │   ├── layer_funcs.cpython-36.pyc
    │   ├── optimizers.cpython-36.pyc
    │   └── reg_funcs.cpython-36.pyc
    ├── cifar_utils.py
    ├── image_generator.py
    ├── layer_funcs.py
    ├── neuralnets
    │   ├── __pycache__
    │   │   └── mlp.cpython-36.pyc
    │   ├── cnn
    │   │   ├── LeNet_trainer.py
    │   │   ├── __pycache__
    │   │   │   ├── LeNet_trainer.cpython-36.pyc
    │   │   │   ├── model_LeNet.cpython-36.pyc
    │   │   │   ├── my_LeNet_trainer.cpython-36.pyc
    │   │   │   └── my_model_LeNet.cpython-36.pyc
    │   │   ├── model_LeNet.py
    │   │   ├── my_LeNet_trainer.py
    │   │   └── my_model_LeNet.py
    │   └── mlp.py
    ├── notebook_images
    │   ├── Task3_2_2_metrics.png
    │   ├── task3_1.jpg
    │   ├── task3_2_1.png
    │   ├── task3_2_2.png
    │   └── task3_2_answer.png
    ├── optimizers.py
    └── reg_funcs.py

537 directories, 847 files
