# Whistler wave simulation repository
This repository hosts whistler wave simulation code, which was used to generate synthetic whistlers with noise. These simulated whistler waves closely resemble actual whistlers with respect to the attributes needed to train machine-learning models. The example result plot for this code is shown below with the label 'Synthetic whistler with noise', whereas the label 'Real whistler with noise' shows an actual measured whistler wave with noise. Since whistler waves are most useful in real-time applications, a YOLOv3 deep-learning model was trained exclusively on these synthetic whistlers and used on actual whistlers. The model showed good results with regard to real whistler attributes; however, the model seemed to overfit with respect to augmentation techniques used to increase the size of the dataset. These arising problems will be discussed in the paper currently being written, to be referenced by the end of September 2023. This study was funded by the South African National Space Agency in conjunction with the School of Chemistry and Physics at the University of Kwa-Zulu-Natal, where a dissertation was submitted.
                               |![Alt text](real_detected_whistler.jpg?raw=true "Actual whistler")|
|:--:| 
| *Real whistler wave* |
|![Alt text](simulated_whistler.jpg?raw=true "Actual whistler")|
|:--:| 
| *Synthetic whistler with noise* |

