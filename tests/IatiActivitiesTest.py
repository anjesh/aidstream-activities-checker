import unittest
import sys

from IatiActivities import *

class IatiActivities1Test(unittest.TestCase):
    def setUp(self):
        self.rowData = ['1706', 'Rahnuma-Family Planning Association of Pakistan', 'mis@fpapak.org', 'en', 'PKR', '2015-01-28 15:49:13', 'Rahnuma-Family Planning Assocation of Pakistan', 'PK-MSW-633-1965', '22', 'PK-MSW-633-1965-GPAF-IMP-059', 'Integrating Education Health and Income generation services for 14,000 school students, their mothers and families, in Pakistan.', '[4]Published', 'This is a synergistic project, connecting three ongoing initiatives related to Sexual and Reproductive Health education, services and improving livelihoods. Using the platform of schools, the project will reach out to adolescents, their mothers and families in ten districts of Pakistan, to increase knowledge and access to nutrition and Sexual and Reproductive Health services, improve health and education outcomes, as well as to empower women and benefit deserving families through enhancement of their employment skills and provision of micro-credit facilities for income generation.', '[1]General', '2', '2013-07-01', '', '2016-06-30', '', '0', '0', '0', '354255', ';Department For International Development DFID', '', ';Rahnuma-Family Planning Assocation of Pakistan', ';Rahnuma-Family Planning Assocation of Pakistan', '', 'PK', '', '', '', '', '', 'DAC', '13020', '', '']

    def testTitle(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.TITLE], "Integrating Education Health and Income generation services for 14,000 school students, their mothers and families, in Pakistan.")
        self.assertEqual(row.checkTitle(), True)

    def testDescription(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.DESCRIPTION], "This is a synergistic project, connecting three ongoing initiatives related to Sexual and Reproductive Health education, services and improving livelihoods. Using the platform of schools, the project will reach out to adolescents, their mothers and families in ten districts of Pakistan, to increase knowledge and access to nutrition and Sexual and Reproductive Health services, improve health and education outcomes, as well as to empower women and benefit deserving families through enhancement of their employment skills and provision of micro-credit facilities for income generation.")
        self.assertEqual(self.rowData[IatiCSVRowConstants.DESCRIPTION_TYPE], "[1]General")
        self.assertEqual(row.checkDescription(), True)
        
    def testStartDate(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.START_PLANNED], "2013-07-01")
        self.assertEqual(self.rowData[IatiCSVRowConstants.START_ACTUAL], "")
        self.assertEqual(row.checkStartDate(), True)

    def testStatus(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.ACTIVITY_STATUS], "2")
        self.assertEqual(row.checkActivityStatus(), True)

    def testParticipatingOrg(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.FUNDING_ORGANISATIONS], ";Department For International Development DFID")
        self.assertEqual(self.rowData[IatiCSVRowConstants.IMPLEMENTING_ORGANISATIONS], ";Rahnuma-Family Planning Assocation of Pakistan")
        self.assertEqual(row.checkParticipatingOrg(), True)

    def testSector(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.SECTOR_CODES], "13020")
        self.assertEqual(row.checkSector(), True)

    def testRecipientCountryRegion(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.RECIPIENT_COUNTRY_CODES], "PK")
        self.assertEqual(self.rowData[IatiCSVRowConstants.RECIPIENT_REGION_CODES], "")
        self.assertEqual(row.checkRecipientCountryRegion(), True)

class IatiActivities2Test(unittest.TestCase):
    def setUp(self):
        self.rowData = ['1706', 'Rahnuma-Family Planning Association of Pakistan', 'mis@fpapak.org', 'en', 'PKR', '2015-01-28 15:49:13', 'Rahnuma-Family Planning Assocation of Pakistan', 'PK-MSW-633-1965', '22', 'PK-MSW-633-1965-GPAF-IMP-059', '', '[4]Published', 'This is a synergistic project, connecting three ongoing initiatives related to Sexual and Reproductive Health education, services and improving livelihoods. Using the platform of schools, the project will reach out to adolescents, their mothers and families in ten districts of Pakistan, to increase knowledge and access to nutrition and Sexual and Reproductive Health services, improve health and education outcomes, as well as to empower women and benefit deserving families through enhancement of their employment skills and provision of micro-credit facilities for income generation.', '[1]General;[1]General', '2', '2013-07-01', '', '2016-06-30', '', '0', '0', '0', '354255', ';Department For International Development DFID', '', ';Rahnuma-Family Planning Assocation of Pakistan', ';Rahnuma-Family Planning Assocation of Pakistan', '', 'PK', '', '', '', '', '', 'DAC', '13020', '', '']

    def testTitle(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.TITLE], "")
        self.assertEqual(row.checkTitle(), False)
        self.assertEqual(row.errors.errors[0], "Title missing")

    def testDescription(self):
        row = IatiActivityRow(self.rowData)
        self.assertEqual(self.rowData[IatiCSVRowConstants.DESCRIPTION], "This is a synergistic project, connecting three ongoing initiatives related to Sexual and Reproductive Health education, services and improving livelihoods. Using the platform of schools, the project will reach out to adolescents, their mothers and families in ten districts of Pakistan, to increase knowledge and access to nutrition and Sexual and Reproductive Health services, improve health and education outcomes, as well as to empower women and benefit deserving families through enhancement of their employment skills and provision of micro-credit facilities for income generation.")
        self.assertEqual(self.rowData[IatiCSVRowConstants.DESCRIPTION_TYPE], "[1]General;[1]General")
        self.assertEqual(row.checkDescription(), False)


if __name__ == "__main__":
    unittest.main()

