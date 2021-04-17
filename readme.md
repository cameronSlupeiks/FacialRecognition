# Facial Recognition Program

Cameron Slupeiks - 101013794 <br/> Nicole Laurin: -101042433

## Summary

The goal of our project will be to develop a facial recognition program to detect known andunknown subjects. We will be
using a convolutional neural network, deep metric learning andsome facial recognition libraries to detect and identify
human faces. Through the use of facialfeature extraction and facial encoding, we will be able to identify whether the
subjects detectedin a livestream video are identifiable or not.

## Background

The field of applying computer vision and neural networks into the development andimplementation of facial detection and
recognition has been developing for many years and hasmuch progress to make. Modern software has demonstrated new and
improved uptakes infacial recognition.

In an ideal situation, we would use the Convolutional Neural Network (CNN) for face detection found in `dlib`. The
purpose of using CNN is to use algorithms that will recognize and memorize facial patterns and features from different
angles. The CNN is more costly in runtime compared to the HoG-based detector because it creates and recognizes
non-frontal facial features. Due to low computational capacity and lack of a GPU, we will be using the HoG-based
detector. The dlib library includes many algorithms that will help us detect features from pictures and live streaming
videos. In order to use `dlib` (a C++ library), we will be using the `Face_recognition` library. This library acts as a
wrapper for dlib’s facial recognition functionality, and it is easy to use in practice.

For livestream recognition testing, we will be using the 720p FaceTime HD camera that is built-in to a MacBook Pro
(Mid-2015). This camera generally performs well in good lighting, but it is known to have poor white balance and it
skews colours (e.g. a green wall may look blue or brown). It also does not perform well in low-light - the frames that
are produced are extremely grainy, which means our livestream facial recognition script may not be as efficient in the
dark.

## Challenges

<u>Accuracy</u>

A big challenge we might face will be to gain accurate results. Through the use of machine learning, it is important
that we are able to differentiate features that uniquely represent each individual. We must be able to train the data to
gain the best outcome for classifying the individuals based on facial recognition.

<u>Computing Power</u>

We will be focusing on using colab in order to use the GPU, which will create more computing power and can handle more
processes per second. When running a more demanding and costly model like such, using a GPU-powered server will save us
time when it comes to handling image encoding because it can help handle more tasks simultaneously. Unfortunately, we
will be testing our livestreaming facial recognition script on a MacBook Pro. This will likely result in alower FPS
rate, as this laptop does not contain a GPU to handle heavy graphics-related processes.

## Goals and Deliverables

| Week | Delivery Date | Nicole's Tasks                    | Cameron's Tasks                                                |
| ---- | ------------- | --------------------------------- | -------------------------------------------------------------- |
| 1    | February 20   | Fill out project proposal         | Fill out project proposal                                      |
| 2    | February 28   | Build collab outline              | Find ways to link colab and github or running program on cloud |
| 3    | March 7       | Gather 30 photos                  | Gather 30 photos                                               |
| 4    | March 17      | Develop facial encoder script     | Develop facial encoder script                                  |
| 5    | March 21      | Develop facial encoder script     | Develop facial encoder script                                  |
| 6    | March 28      | Develop facial recognition script | Develop facial recognition script                              |
| 7    | April 4       | Work on presentation + report     | Work on presentation + report                                  |
| 8    | April 14      | Hand in assignment                | Hand in assignment                                             |

## Demo

In order to demo the facial recognition system, run the `demo.sh` BASH script:

```
./demo.sh
```

This will check that the correct Python version is installed, it will install all dependencies, it will run the
`facial_encoder.py` script, then it will run the `facial_recognition.py` script. To exit the facial recognition system,
press `q`.
