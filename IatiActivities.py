import re

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
    ACTIVITY_STATE = 11
    DESCRIPTION = 12
    DESCRIPTION_TYPE = 13
    ACTIVITY_STATUS = 14
    START_PLANNED = 15
    START_ACTUAL = 16
    END_PLANNED = 17
    END_ACTUAL = 18
    TOTAL_COMMITMENTS = 19
    TOTAL_DISBURSEMENTS = 20
    TOTAL_EXPENDITURE = 21
    TOTAL_INCOMING_FUNDS = 22
    FUNDING_ORGANISATIONS = 23
    EXTENDING_ORGANISATIONS = 24
    ACCOUNTABLE_ORGANISATIONS = 25
    IMPLEMENTING_ORGANISATIONS = 26
    RECIPIENT_COUNTRY = 27
    RECIPIENT_COUNTRY_CODES = 28
    RECIPIENT_COUNTRY_PERCENTAGES = 29
    RECIPIENT_REGION = 30
    RECIPIENT_REGION_CODES = 31
    RECIPIENT_REGION_PERCENTAGES = 32
    SECTOR_TEXT = 33
    SECTOR_VOCABULARIES = 34
    SECTOR_CODES = 35
    SECTOR_PERCENTAGES = 36

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
        descriptionType = self.row[IatiCSVRowConstants.DESCRIPTION_TYPE]
        descriptionTypesArray = descriptionType.split(";")
        typeCodes = []
        for dtype in descriptionTypesArray:
            m = re.findall('\[([0-9]*)\].*', dtype)
            if m and m[0]:
                if m[0] in typeCodes:
                    self.errors.add("Descriptions with same type exist")
                    return False
                    break
                else:
                    typeCodes.append(m[0])
        # [1]General;[2]Objectives;[3]Target Groups
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

    





