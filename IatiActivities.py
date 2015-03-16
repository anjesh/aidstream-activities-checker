
class IatiCSVRowConstants:
    ACTIVITY_ID = 0
    ORG_NAME = 1
    ORG_EMAIL = 2
    DEFAULT_LANGUAGE = 3
    DEFAULT_CURRENCY = 4
    LAST_UPDATED_DATETIME = 5
    REPORTING_ORGANISATION = 6
    REPORTING_ORGANISATION_REF = 7
    REPORTING_ORG_TYPE = 8
    IATI_IDENTIFIER = 9
    TITLE = 10
    DESCRIPTION = 11
    ACTIVITY_STATUS = 12
    START_PLANNED = 13
    START_ACTUAL = 14
    END_PLANNED = 15
    END_ACTUAL = 16
    TOTAL_COMMITMENTS = 17
    TOTAL_DISBURSEMENTS = 18
    TOTAL_EXPENDITURE = 19
    TOTAL_INCOMING_FUNDS = 20
    FUNDING_ORGANISATIONS = 21
    EXTENDING_ORGANISATIONS = 22
    ACCOUNTABLE_ORGANISATIONS = 23
    IMPLEMENTING_ORGANISATIONS = 24
    RECIPIENT_COUNTRY = 25
    RECIPIENT_COUNTRY_CODES = 26
    RECIPIENT_COUNTRY_PERCENTAGES = 27
    RECIPIENT_REGION = 28
    RECIPIENT_REGION_CODES = 29
    RECIPIENT_REGION_PERCENTAGES = 30
    SECTOR_TEXT = 31
    SECTOR_VOCABULARIES = 32
    SECTOR_CODES = 33
    SECTOR_PERCENTAGES = 34

class ErrorLogs:
    def __init__(self):
        self.errors = []
        pass

    def add(self, log):
        self.errors.append(log)

class IatiActivityRow:
    def __init__(self, row):
        self.row = row        
        self.errors = ErrorLogs()

    def hasError(self):
        return True if len(self.errors.errors) else False

    def getErrors(self):
        return ";".join(self.errors.errors)

    def getFieldValue(self, field):
        return self.row[field]

    def process(self):
        self.checkTitle()
        self.checkDescription()
        self.checkStartDate()
        self.checkActivityStatus()
        self.checkParticipatingOrg()
        self.checkSector()
        self.checkRecipientCountryRegion() 

    def checkTitle(self):
        title = self.row[IatiCSVRowConstants.TITLE]
        if len(title.strip()):            
            return True
        self.errors.add("Title missing")
        return False

    def checkDescription(self):
        description = self.row[IatiCSVRowConstants.DESCRIPTION]
        if len(description.strip()):
            return True
        self.errors.add("Description missing")
        return False

    def checkStartDate(self):
        startPlanned = self.row[IatiCSVRowConstants.START_PLANNED]
        startActual = self.row[IatiCSVRowConstants.START_ACTUAL]
        if(len(startActual) or len(startPlanned)):
            return True
        self.errors.add("Starting date missing")
        return False

    def checkActivityStatus(self):
        status = self.row[IatiCSVRowConstants.ACTIVITY_STATUS]
        if status:
            return True
        self.errors.add("Status missing")
        return False

    def checkParticipatingOrg(self):
        fundingOrg = self.row[IatiCSVRowConstants.FUNDING_ORGANISATIONS]
        implementingOrg = self.row[IatiCSVRowConstants.IMPLEMENTING_ORGANISATIONS]
        if fundingOrg or implementingOrg:
            return True
        self.errors.add("Both implementing and funding organisation are missing")
        return False

    def checkSector(self):
        sectorCodes = self.row[IatiCSVRowConstants.SECTOR_CODES]
        if sectorCodes:
            return True
        self.errors.add("Sectors missing")
        return False

    def checkRecipientCountryRegion(self):
        countryCodes = self.row[IatiCSVRowConstants.RECIPIENT_COUNTRY_CODES]
        regionCodes = self.row[IatiCSVRowConstants.RECIPIENT_REGION_CODES]
        if countryCodes and regionCodes:
            self.errors.add("Both Recipient Countries and Regions are present")
            return False
        if (not countryCodes) and (not regionCodes):
            self.errors.add("Both Recipient Countries and Regions are missing")
            return False
        return True

    





