
class SymbolOptions:
    def __init__(self):
        self.quantity = ""  # FieldID C
        self.reinforcedReduced = ""  # FieldID F
        self.staffComments = ""  # FieldID G
        self.additionalInformation = ""  # FieldID H
        self.evaluationRating = ""  # FieldID J
        self.combatEffectiveness = ""  # FieldID K
        self.signatureEquipment = ""  # FieldID L
        self.higherFormation = ""  # FieldID M
        self.hostile = ""  # FieldID N
        self.iffSif = ""  # FieldID P
        self.direction = ""  # FieldID Q
        self.sigint = ""  # FieldID R2
        self.uniqueDesignation = ""  # FieldID T
        self.type = ""  # FieldID V
        self.dtg = ""  # FieldID W
        self.altitudeDepth = ""  # FieldID X
        self.location = ""  # FieldID Y
        self.speed = ""  # FieldID Z
        self.speedLeader = 0  # This is the length of the speed leader
        self.specialHeadquarters = ""  # FieldID AA
        self.country = ""  # AC Country
        self.platformType = ""  # FieldID AD
        self.equipmentTeardownTime = ""  # FieldID AE
        self.commonIdentifier = ""  # FieldID AF
        self.auxiliaryEquipmentIndicator = ""  # FieldID AG
        self.headquartersElement = ""  # FieldID AH
        self.installationComposition = ""  # FieldID AI
        # FieldID AM Distance
        # FieldID AN Azimuth
        self.engagementBar = ""  # FieldID AO EngagementBar
        self.engagementType = ""  # Engagement Bar Type, should be one of "TARGET", "NON-TARGET", or "EXPIRED"
        self.guardedUnit = ""  # FieldID AQ
        self.specialDesignator = ""  # FieldID AR
        self.sidc = ""


class SymbolStyle:
    def __init__(self):
        self.alternateMedal = False  # 2525D lets you choose between MEDAL icn and alternate MEDAL icn for Mines; default is set to MEDAL.
        self.civilianColor = True  # Should we use the Civilian Purple defined in 2525? (We set this to default because I like the color.
        self.colorMode = "Light"  # 2525C Allows you to use Dark; Medium or Light colors. The values you can set are "Dark";"Medium" or "Light"
        self.fill = True  # Should the icon be filled with color
        self.fillColor = ""  # Override the frame fill with any color
        self.fillOpacity = 1  # Possibility to change the fill opacity
        self.fontfamily = "Arial"  # The font family to use
        self.frame = True  # Should the icon be framed
        self.frameColor = ""
        self.hqStaffLength = 0  # The default length of the HQ staf
        self.icon = True  # Should we display the icon?
        self.iconColor = ""
        self.infoBackground = ""  # Color of square behind texts
        self.infoBackgroundFrame = ""  # Color of the squares frame
        self.infoColor = ""  # Changes the color of the info fields
        self.infoFields = True  # If you have set all info fields but don't want the displayed; then just set this to false.
        self.infoOutlineColor = "rgb(239, 239, 239)"  # Color of the text outline.
        self.infoOutlineWidth = False  # Width of the text-field outline.
        self.infoSize = 40  # Relative size of the info fields
        self.monoColor = ""  # Should the icon be monocromatic and if so what color
        self.outlineColor = "rgb(239, 239, 239)"  # Color of the outline
        self.outlineWidth = 0  # Width of the outline.
        self.padding = 0  # Extra padding around the symbol
        self.simpleStatusModifier = False  # Force use of simple status modifiers
        self.size = 100  # The symbol size is actually the L variable in the symbols so the symbol will be larger than this size.
        self.square = False  # If the symbol should be square
        self.standard = ""  # Set standard override
        self.strokeWidth = 4  # The stroke width of he icon frame.
