# Copyright (c) 2020 Yannan Wu
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#========================================================================
PLUG_IN_ACCURACY = 0   # Please set the accuracy of your plug-in here
#========================================================================

class PlugInWrapper:
    # an estimation plug-in wrapper class that implements the necessary interface functions for Accelergy-Plugin communications

    # -------------------------------------------------------------------------------------
    # Interface functions below,
    #   function name, input arguments, and output format CANNOT be changed
    # -------------------------------------------------------------------------------------
    def __init__(self):

        """" initialize function that will be called inside Accelergy to instantiate the estimation plug-in"""
        self.estimator_name =  "my_plug_in"  # please enter your plug-in's name here

    def primitive_action_supported(self, interface):
        """interface function for checking if a component action is supported by this plug-in"""

        # this function is called inside Accelergy as the initial check to see whether a component action is supported

        # ================
        # Input
        # ================
        # `interface` input is a dictionary that contains 4 keys:
        # (1) class_name: the value for this key is a string that describes the name of the primitive component class
        # (2) attributes: the value for this key is another dictionary that
        #                 describes the attributes name-value pairs of the primitive component under evaluation
        # (3) action_name: the value for this key is a string that describes the name of the primitive action under evaluation
        # (4) arguments: the value for this key is another dictionary that
        #                describes the arguments name-value pairs (if any) of the primitive action under evaluation


        # ================
        # Output
        # ================
        # If the plug-in suppor the specific request sent from Accelergy
        #    this function should be the accuracy of the estimation plug-in,
        # if not supported, please return 0

        # example extractions of the information provided in the interface
        class_name = interface['class_name']
        attributes = interface['attributes']
        action_name = interface['action_name']
        arguments = interface['arguments']


        return PLUG_IN_ACCURACY # if not supported, please return 0

    def estimate_energy(self, interface):
        """ Interface function for performing the actual energy estimations of the request sent from Accelergy"""

        # this function will only be called if this plug-in is selected to be the most accurate plug-in by Accelergy,
        # it should perform the energy estimation for the request

        # ================
        # Input
        # ================
        # `interface` input contains the same information as described in the `primitive_action_supported` function,
        #     please refer back to the comments above

        # ================
        # Output
        # ================
        # please return the estimated energy
        # note that this value will be rounded inside Accelergy,
        #       default rounding is 3 decimal points, but precision can be set via the -d flag when running Accelergy

        return 0.0

    def primitive_area_supported(self, interface):
        """interface function for checking if a component's area is supported by this plug-in"""

        # input and output of this function format is the same as the `primitive_action_supported` function
        # note that this is a check for area estimation instead of energy estimation;
        #      if this plug-in does not support area estimation sof components, zero should be returned

        return PLUG_IN_ACCURACY # if not supported, please return 0


    def estimate_area(self, interface):
        """ Interface function for performing the actual area estimations of the request sent from Accelergy"""
        # input and output of this function is the same format as the `estimate_energy` function

        return 0