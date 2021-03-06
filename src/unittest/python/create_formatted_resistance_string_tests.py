import unittest
from resistor import *

class CreateFormattedResistanceStringTests(unittest.TestCase):

    def testCreateFormattedResistanceStringFourBandRedBrownBlackBrown(self):
        colors = ['red', 'brown', 'black', 'brown']
        result = createFormattedResistanceString(colors)
        self.assertEquals("21 ohms +/- 1.0%", result)

    def testCreateFormattedResistanceStringFourBandGreenBlueBrownRed(self):
        colors = ['green', 'blue', 'brown', 'red']
        result = createFormattedResistanceString(colors)
        self.assertEquals("560 ohms +/- 2.0%", result)
    
    def testCreateFormattedResistanceStringFourBandVioletGreyRedGreen(self):
        colors = ['violet', 'grey', 'red', 'green']
        result = createFormattedResistanceString(colors)
        self.assertEquals("7.8 Kohms +/- 0.5%", result)
    
    def testCreateFormattedResistanceStringFourBandWhiteOrangeOrangeBlue(self):
        colors = ['white', 'orange', 'orange', 'blue']
        result = createFormattedResistanceString(colors)
        self.assertEquals("93 Kohms +/- 0.25%", result)
    
    def testCreateFormattedResistanceStringFourBandRedGreyYellowViolet(self):
        colors = ['red', 'grey', 'yellow', 'violet']
        result = createFormattedResistanceString(colors)
        self.assertEquals("280 Kohms +/- 0.1%", result)

    def testCreateFormattedResistanceStringFourBandBlueOrangeGreenGrey(self):
        colors = ['blue', 'orange', 'green', 'grey']
        result = createFormattedResistanceString(colors)
        self.assertEquals("6.3 Mohms +/- 0.05%", result)

    def testCreateFormattedResistanceStringFourBandGreenWhiteBlueGold(self):
        colors = ['green', 'white', 'blue', 'gold']
        result = createFormattedResistanceString(colors)
        self.assertEquals("59 Mohms +/- 5.0%", result)

    def testCreateFormattedResistanceStringFourBandVioletRedVioletSilver(self):
        colors = ['violet', 'red', 'violet', 'silver']
        result = createFormattedResistanceString(colors)
        self.assertEquals("720 Mohms +/- 10.0%", result)

    def testCreateFormattedResistanceStringFourBandVioletRedVioletNone(self):
        colors = ['violet', 'red', 'violet', 'none']
        result = createFormattedResistanceString(colors)
        self.assertEquals("720 Mohms +/- 20.0%", result)

    def testCreateFormattedResistanceStringFourBandGreyBlackGreyBrown(self):
        colors = ['grey', 'black', 'grey', 'brown']
        result = createFormattedResistanceString(colors)
        self.assertEquals("8.0 Gohms +/- 1.0%", result)

    def testCreateFormattedResistanceStringFourBandOrangeBlueWhiteRed(self):
        colors = ['orange', 'blue', 'white', 'red']
        result = createFormattedResistanceString(colors)
        self.assertEquals("36 Gohms +/- 2.0%", result)

    def testCreateFormattedResistanceStringFourBandVioletVioletGoldGreen(self):
        colors = ['violet', 'violet', 'gold', 'green']
        result = createFormattedResistanceString(colors)
        self.assertEquals("7.7 ohms +/- 0.5%", result)

    def testCreateFormattedResistanceStringFourBandWhiteBlackSilverBlue(self):
        colors = ['white', 'black', 'silver', 'blue']
        result = createFormattedResistanceString(colors)
        self.assertEquals("0.9 ohms +/- 0.25%", result)

    def testCreateFormattedResistanceStringFiveBandRedOrangeBlackBlackBrown(self):
        colors = ['red', 'orange', 'black', 'black', 'brown']
        result = createFormattedResistanceString(colors)
        self.assertEquals("230 ohms +/- 1.0%", result)

    def testCreateFormattedResistanceStringFiveBandGreenYellowRedBrownRed(self):
        colors = ['green', 'yellow', 'red', 'brown', 'red']
        result = createFormattedResistanceString(colors)
        self.assertEquals("5.42 Kohms +/- 2.0%", result)

    def testCreateFormattedResistanceStringFiveBandBrownRedVioletRedGreen(self):
        colors = ['brown', 'red', 'violet', 'red', 'green']
        result = createFormattedResistanceString(colors)
        self.assertEquals("12.7 Kohms +/- 0.5%", result)

    def testCreateFormattedResistanceStringFiveBandBlueRedGreenOrangeBlue(self):
        colors = ['blue', 'red', 'green', 'orange', 'blue']
        result = createFormattedResistanceString(colors)
        self.assertEquals("625 Kohms +/- 0.25%", result)

    def testCreateFormattedResistanceStringFiveBandBrownRedVioletYellowViolet(self):
        colors = ['brown', 'red', 'violet', 'yellow', 'violet']
        result = createFormattedResistanceString(colors)
        self.assertEquals("1.27 Mohms +/- 0.1%", result)

    def testCreateFormattedResistanceStringFiveBandBlueRedGreenGreenGrey(self):
        colors = ['blue', 'red', 'green', 'green', 'grey']
        result = createFormattedResistanceString(colors)
        self.assertEquals("62.5 Mohms +/- 0.05%", result)

    def testCreateFormattedResistanceStringFiveBandBlueGreenBlueBlueGold(self):
        colors = ['blue', 'green', 'blue', 'blue', 'gold']
        result = createFormattedResistanceString(colors)
        self.assertEquals("656 Mohms +/- 5.0%", result)

    def testCreateFormattedResistanceStringFiveBandBrownRedOrangeVioletSilver(self):
        colors = ['brown', 'red', 'orange', 'violet', 'silver']
        result = createFormattedResistanceString(colors)
        self.assertEquals("1.23 Gohms +/- 10.0%", result)

    def testCreateFormattedResistanceStringFiveBandVioletVioletVioletGreyNone(self):
        colors = ['violet', 'violet', 'violet', 'grey', 'none']
        result = createFormattedResistanceString(colors)
        self.assertEquals("77.7 Gohms +/- 20.0%", result)

    def testCreateFormattedResistanceStringFiveBandBrownRedVioletWhiteBrown(self):
        colors = ['brown', 'red', 'violet', 'white', 'brown']
        result = createFormattedResistanceString(colors)
        self.assertEquals("127 Gohms +/- 1.0%", result)

    def testCreateFormattedResistanceStringFiveBandBlueGreenBlueGoldRed(self):
        colors = ['blue', 'green', 'blue', 'gold', 'red']
        result = createFormattedResistanceString(colors)
        self.assertEquals("65.6 ohms +/- 2.0%", result)

    def testCreateFormattedResistanceStringFiveBandBrownRedOrangeSilverGreen(self):
        colors = ['brown', 'red', 'orange', 'silver', 'green']
        result = createFormattedResistanceString(colors)
        self.assertEquals("1.23 ohms +/- 0.5%", result)