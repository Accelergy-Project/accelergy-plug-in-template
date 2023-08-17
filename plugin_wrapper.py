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
from accelergy.plug_in_interface.estimator_wrapper import (
    AccelergyPlugIn,
    AccelergyQuery,
    AccuracyEstimation,
    Estimation
)


class PlugIn(AccelergyPlugIn):
    """ 
    Example plug-in for Accelergy. Extend me!
    For logging within the plug-in, DO NOT use print statements. Instead, use
    self.logger.info(), self.logger.warning(), self.logger.error(), etc.
    """

    def __init__(self):
        super().__init__()
        self.myvar = 5  # add any initialization here

    def action_supported(self, query: AccelergyQuery) -> AccuracyEstimation:
        """ 
        Returns an AccuracyEstimation with the percent accuracy of the
        plug-in's ability to estimate the action represented by the query.
        Returns AccuracyEstimation(0) or raises an exception if the plug-in
        cannot estimate the action.
        """
        class_name = query.class_name
        attributes = query.attributes
        action_name = query.action_name
        arguments = query.arguments
        self.logger.info('Accuracy check for %s %s', class_name, action_name)
        accuracy_0_100 = 70
        return AccuracyEstimation(accuracy_0_100)

    def estimate_energy(self, query: AccelergyQuery) -> Estimation:
        """
        Returns an Estimation with the energy of the action represented by the
        query. Raises an exception if the plug-in cannot estimate the action.
        """
        class_name = query.class_name
        attributes = query.attributes
        action_name = query.action_name
        arguments = query.arguments
        self.logger.info('Estimating %s %s', class_name, action_name)
        return Estimation(123, 'p')  # 123 pJ

    def primitive_area_supported(self, query: AccelergyQuery) -> AccuracyEstimation:
        """
        Returns an AccuracyEstimation with the percent accuracy of the
        plug-in's ability to estimate the area of the primitive represented by
        the query. Returns AccuracyEstimation(0) or raises an exception if the
        plug-in cannot estimate the area.
        """
        class_name = query.class_name
        attributes = query.attributes
        self.logger.info('Accuracy check for %s area', class_name)
        accuracy_0_100 = 70
        return AccuracyEstimation(accuracy_0_100)

    def estimate_area(self, query: AccelergyQuery) -> Estimation:
        """
        Returns an Estimation with the area of the primitive represented by the
        query. Raises an exception if the plug-in cannot estimate the area.
        """
        class_name = query.class_name
        attributes = query.attributes
        self.logger.info('Estimating %s area', class_name)
        return Estimation(123, 'u^2')  # 123 um^2

    def get_name(self) -> str:
        """
        Returns the name of the plug-in.
        """
        return "Example Plug-in"
