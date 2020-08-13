# Deep Q Learning Experiments

This repo contains my first foray into Deep Q Learning. Here I apply it to the
process of image tagging. The problem consists of arbitrarily sized images with
arbitrary content that must can be tagged with any of several hundred tags.

## Introduction

The planned strategy is to create an environment consisting of a number of
windows. These windows each maintain a position and zoom level. At any time,
they return a 64x64 pixel representation of the image based on their current
position and zoom level. The actions that can be performed on the environment
are to translate or zoom any window.

Each window is attached to a conv net used for feature extraction which then
feeds into a deep neural network to produce a set of tags. The idea is to group
related tags under the same window, hopefully increasing accuracy and
performance.

This approach was taken as a way to avoid losing the information provided in a
high resolution image while also minimizing the computing costs. Since typical
image dimensions are 3508x4961 pixels, in full color, that yields a total of
52,209,564 variables in state. In contrast, even if a window is used for each
tag, at 200 tags, this yields 600 variables in state (each window has 3
parameters: x, y, and zoom). The significance of the difference cannot be
exaggerated.
