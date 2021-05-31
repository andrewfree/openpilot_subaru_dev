# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CarControllerParams:
  HCA_STEP = 2                   # HCA_01 message frequency 50Hz
  LDW_STEP = 10                  # LDW_02 message frequency 10Hz
  GRA_ACC_STEP = 3               # GRA_ACC_01 message frequency 33Hz

  GRA_VBP_STEP = 100             # Send ACC virtual button presses once a second
  GRA_VBP_COUNT = 16             # Send VBP messages for ~0.5s (GRA_ACC_STEP * 16)

  # Observed documented MQB limits: 3.00 Nm max, rate of change 5.00 Nm/sec.
  # Limiting rate-of-change based on real-world testing and Comma's safety
  # requirements for minimum time to lane departure.
  STEER_MAX = 300                # Max heading control assist torque 3.00 Nm
  STEER_DELTA_UP = 4             # Max HCA reached in 1.50s (STEER_MAX / (50Hz * 1.50))
  STEER_DELTA_DOWN = 10          # Min HCA reached in 0.60s (STEER_MAX / (50Hz * 0.60))
  STEER_DRIVER_ALLOWANCE = 80
  STEER_DRIVER_MULTIPLIER = 3    # weight driver torque heavily
  STEER_DRIVER_FACTOR = 1        # from dbc

class CANBUS:
  pt = 0
  cam = 2

TransmissionType = car.CarParams.TransmissionType
GearShifter = car.CarState.GearShifter

BUTTON_STATES = {
  "accelCruise": False,
  "decelCruise": False,
  "cancel": False,
  "setCruise": False,
  "resumeCruise": False,
  "gapAdjustCruise": False
}

MQB_LDW_MESSAGES = {
  "none": 0,                            # Nothing to display
  "laneAssistUnavailChime": 1,          # "Lane Assist currently not available." with chime
  "laneAssistUnavailNoSensorChime": 3,  # "Lane Assist not available. No sensor view." with chime
  "laneAssistTakeOverUrgent": 4,        # "Lane Assist: Please Take Over Steering" with urgent beep
  "emergencyAssistUrgent": 6,           # "Emergency Assist: Please Take Over Steering" with urgent beep
  "laneAssistTakeOverChime": 7,         # "Lane Assist: Please Take Over Steering" with chime
  "laneAssistTakeOverSilent": 8,        # "Lane Assist: Please Take Over Steering" silent
  "emergencyAssistChangingLanes": 9,    # "Emergency Assist: Changing lanes..." with urgent beep
  "laneAssistDeactivated": 10,          # "Lane Assist deactivated." silent with persistent icon afterward
}

# Check the 7th and 8th characters of the VIN before adding a new CAR. If the
# chassis code is already listed below, don't add a new CAR, just add to the
# FW_VERSIONS for that existing CAR.

class CAR:
  ATLAS_MK1 = "VOLKSWAGEN ATLAS 1ST GEN"      # Chassis CA, Mk1 VW Atlas and Atlas Cross Sport
  GOLF_MK7 = "VOLKSWAGEN GOLF 7TH GEN"        # Chassis 5G/AU/BA/BE, Mk7 VW Golf and variants
  JETTA_MK7 = "VOLKSWAGEN JETTA 7TH GEN"      # Chassis BU, Mk7 Jetta
  PASSAT_MK8 = "VOLKSWAGEN PASSAT 8TH GEN"    # Chassis 3G, Mk8 Passat and variants
  TIGUAN_MK2 = "VOLKSWAGEN TIGUAN 2ND GEN"    # Chassis AD/BW, Mk2 VW Tiguan and variants
  AUDI_A3_MK3 = "AUDI A3 3RD GEN"             # Chassis 8V/FF, Mk3 Audi A3 and variants
  SEAT_ATECA_MK1 = "SEAT ATECA 1ST GEN"       # Chassis 5F, Mk1 SEAT Ateca and CUPRA Ateca
  SKODA_KODIAQ_MK1 = "SKODA KODIAQ 1ST GEN"   # Chassis NS, Mk1 Skoda Kodiaq
  SKODA_SCALA_MK1 = "SKODA SCALA 1ST GEN"     # Chassis NW, Mk1 Skoda Scala and Skoda Kamiq
  SKODA_SUPERB_MK3 = "SKODA SUPERB 3RD GEN"   # Chassis 3V/NP, Mk3 Skoda Superb and variants
  SKODA_OCTAVIA_MK3 = "SKODA OCTAVIA 3RD GEN" # Chassis NE, Mk3 Skoda Octavia and variants

FW_VERSIONS = {
  CAR.ATLAS_MK1: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8703H906026AA\xf1\x899970',
      b'\xf1\x8703H906026F \xf1\x899970',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x8709G927158A \xf1\x893387',
      b'\xf1\x8709G927158DR\xf1\x893536',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x873Q0959655BC\xf1\x890503\xf1\x82\0161914151912001103111122031200',
      b'\xf1\x873Q0959655BN\xf1\x890713\xf1\x82\0162214152212001105141122052900',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x873QF909144B \xf1\x891582\xf1\x82\00571B60924A1',
      b'\xf1\x875Q0909143P \xf1\x892051\xf1\x820528B6090105',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572H \xf1\x890620',
      b'\xf1\x875Q0907572P \xf1\x890682',
    ],
  },
  CAR.GOLF_MK7: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906016A \xf1\x897697',
      b'\xf1\x8704E906016AD\xf1\x895758',
      b'\xf1\x8704E906023AG\xf1\x891726',
      b'\xf1\x8704E906023BN\xf1\x894518',
      b'\xf1\x8704E906027GR\xf1\x892394',
      b'\xf1\x8704E906027MA\xf1\x894958',
      b'\xf1\x8704L906026NF\xf1\x899528',
      b'\xf1\x8704L906056CR\xf1\x895813',
      b'\xf1\x8704L906056HE\xf1\x893758',
      b'\xf1\x870EA906016A \xf1\x898343',
      b'\xf1\x870EA906016F \xf1\x895002',
      b'\xf1\x870EA906016S \xf1\x897207',
      b'\xf1\x875G0906259  \xf1\x890007',
      b'\xf1\x875G0906259J \xf1\x890002',
      b'\xf1\x875G0906259L \xf1\x890002',
      b'\xf1\x875G0906259N \xf1\x890003',
      b'\xf1\x875G0906259Q \xf1\x890002',
      b'\xf1\x875G0906259Q \xf1\x892313',
      b'\xf1\x878V0906259J \xf1\x890003',
      b'\xf1\x878V0906259P \xf1\x890001',
      b'\xf1\x878V0906259Q \xf1\x890002',
      b'\xf1\x878V0906264F \xf1\x890003',
      b'\xf1\x878V0906264L \xf1\x890002',
      b'\xf1\x878V0906264M \xf1\x890001',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x8709G927749AP\xf1\x892943',
      b'\xf1\x870CW300041H \xf1\x891010',
      b'\xf1\x870CW300042F \xf1\x891604',
      b'\xf1\x870CW300045  \xf1\x894531',
      b'\xf1\x870CW300047D \xf1\x895261',
      b'\xf1\x870CW300048J \xf1\x890611',
      b'\xf1\x870D9300012  \xf1\x894913',
      b'\xf1\x870D9300014M \xf1\x895004',
      b'\xf1\x870D9300020S \xf1\x895201',
      b'\xf1\x870D9300040S \xf1\x894311',
      b'\xf1\x870DD300045K \xf1\x891120',
      b'\xf1\x870DD300046F \xf1\x891601',
      b'\xf1\x870GC300012A \xf1\x891403',
      b'\xf1\x870GC300014B \xf1\x892401',
      b'\xf1\x870GC300014B \xf1\x892405',
      b'\xf1\x870GC300020G \xf1\x892401',
      b'\xf1\x870GC300020G \xf1\x892403',
      b'\xf1\x870GC300020G \xf1\x892404',
      b'\xf1\x870GC300043T \xf1\x899999',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655AA\xf1\x890386\xf1\x82\0211413001113120043114317121C111C9113',
      b'\xf1\x875Q0959655AA\xf1\x890386\xf1\x82\0211413001113120053114317121C111C9113',
      b'\xf1\x875Q0959655AA\xf1\x890388\xf1\x82\0211413001113120043114317121C111C9113',
      b'\xf1\x875Q0959655AA\xf1\x890388\xf1\x82\0211413001113120043114417121411149113',
      b'\xf1\x875Q0959655AA\xf1\x890388\xf1\x82\0211413001113120053114317121C111C9113',
      b'\xf1\x875Q0959655BH\xf1\x890336\xf1\x82\02314160011123300314211012230229333463100',
      b'\xf1\x875Q0959655BT\xf1\x890403\xf1\x82\023141600111233003142405A2252229333463100',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\023271112111312--071104171825102591131211',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\023271212111312--071104171838103891131211',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\023341512112212--071104172328102891131211',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\x13272512111312--07110417182C102C91131211',
      b'\xf1\x875Q0959655M \xf1\x890361\xf1\x82\0211413001112120041114115121611169112',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\02315120011211200621143171717111791132111',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\02324230011211200061104171724102491132111',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\02324230011211200621143171724112491132111',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\x1315120011211200061104171717101791132111',
      b'\xf1\x875Q0959655T \xf1\x890830\xf1\x82\x13271100111312--071104171826102691131211',
      b'\xf1\x875QD959655  \xf1\x890388\xf1\x82\x111413001113120006110417121D101D9112',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x873Q0909144F \xf1\x895043\xf1\x82\00561A01612A0',
      b'\xf1\x873Q0909144H \xf1\x895061\xf1\x82\00566A0J612A1',
      b'\xf1\x873Q0909144J \xf1\x895063\xf1\x82\00566A00514A1',
      b'\xf1\x873Q0909144K \xf1\x895072\xf1\x82\00571A0J714A1',
      b'\xf1\x873Q0909144L \xf1\x895081\xf1\x82\x0571A0JA15A1',
      b'\xf1\x873Q0909144M \xf1\x895082\xf1\x82\00571A01A18A1',
      b'\xf1\x873Q0909144M \xf1\x895082\xf1\x82\00571A0JA16A1',
      b'\xf1\x875Q0909143K \xf1\x892033\xf1\x820519A9040203',
      b'\xf1\x875Q0909144AA\xf1\x891081\xf1\x82\00521A00441A1',
      b'\xf1\x875Q0909144AA\xf1\x891081\xf1\x82\x0521A00641A1',
      b'\xf1\x875Q0909144AB\xf1\x891082\xf1\x82\00521A00642A1',
      b'\xf1\x875Q0909144AB\xf1\x891082\xf1\x82\00521A07B05A1',
      b'\xf1\x875Q0909144L \xf1\x891021\xf1\x82\00522A00402A0',
      b'\xf1\x875Q0909144P \xf1\x891043\xf1\x82\00511A00403A0',
      b'\xf1\x875Q0909144R \xf1\x891061\xf1\x82\00516A00604A1',
      b'\xf1\x875Q0909144S \xf1\x891063\xf1\x82\00516A07A02A1',
      b'\xf1\x875Q0909144T \xf1\x891072\xf1\x82\00521A20B03A1',
      b'\xf1\x875QD909144B \xf1\x891072\xf1\x82\x0521A00507A1',
      b'\xf1\x875QM909144A \xf1\x891072\xf1\x82\x0521A20B03A1',
      b'\xf1\x875QN909144A \xf1\x895081\xf1\x82\00571A01A18A1',
      b'\xf1\x875QN909144A \xf1\x895081\xf1\x82\x0571A01A17A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572A \xf1\x890141\xf1\x82\00101',
      b'\xf1\x875Q0907572B \xf1\x890200\xf1\x82\00101',
      b'\xf1\x875Q0907572C \xf1\x890210\xf1\x82\00101',
      b'\xf1\x875Q0907572D \xf1\x890304\xf1\x82\00101',
      b'\xf1\x875Q0907572F \xf1\x890400\xf1\x82\00101',
      b'\xf1\x875Q0907572G \xf1\x890571',
      b'\xf1\x875Q0907572H \xf1\x890620',
      b'\xf1\x875Q0907572J \xf1\x890654',
      b'\xf1\x875Q0907572P \xf1\x890682',
    ],
  },
  CAR.JETTA_MK7: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906024AK\xf1\x899937',
      b'\xf1\x8704E906024AS\xf1\x899912',
      b'\xf1\x8704E906024B \xf1\x895594',
      b'\xf1\x8704E906024L \xf1\x895595',
      b'\xf1\x8704E906027MS\xf1\x896223',
      b'\xf1\x875G0906259T \xf1\x890003',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x8709G927158BQ\xf1\x893545',
      b'\xf1\x8709S927158BS\xf1\x893642',
      b'\xf1\x8709S927158R \xf1\x893552',
      b'\xf1\x8709S927158R \xf1\x893587',
      b'\xf1\x870GC300020N \xf1\x892803',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655AG\xf1\x890336\xf1\x82\02314171231313500314611011630169333463100',
      b'\xf1\x875Q0959655BM\xf1\x890403\xf1\x82\02314171231313500314643011650169333463100',
      b'\xf1\x875Q0959655BM\xf1\x890403\xf1\x82\02314171231313500314642011650169333463100',
      b'\xf1\x875Q0959655BR\xf1\x890403\xf1\x82\02311170031313300314240011150119333433100',
      b'\xf1\x875Q0959655BR\xf1\x890403\xf1\x82\02319170031313300314240011550159333463100',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875QM909144B \xf1\x891081\xf1\x82\00521A10A01A1',
      b'\xf1\x875QM909144B \xf1\x891081\xf1\x82\x0521B00404A1',
      b'\xf1\x875QM909144C \xf1\x891082\xf1\x82\00521A00642A1',
      b'\xf1\x875QM909144C \xf1\x891082\xf1\x82\00521A10A01A1',
      b'\xf1\x875QN909144B \xf1\x895082\xf1\x82\00571A10A11A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572N \xf1\x890681',
      b'\xf1\x875Q0907572R \xf1\x890771',
    ],
  },
  CAR.PASSAT_MK8: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906023AH\xf1\x893379',
      b'\xf1\x8704L906026GA\xf1\x892013',
      b'\xf1\x873G0906264  \xf1\x890004',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870CW300048R \xf1\x890610',
      b'\xf1\x870D9300014L \xf1\x895002',
      b'\xf1\x870DD300045T \xf1\x891601',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x873Q0959655AN\xf1\x890306\xf1\x82\r58160058140013036914110311',
      b'\xf1\x873Q0959655BB\xf1\x890195\xf1\x82\r56140056130012026612120211',
      b'\xf1\x875Q0959655S \xf1\x890870\xf1\x82\02315120011111200631145171716121691132111',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909143M \xf1\x892041\xf1\x820522B0080803',
      b'\xf1\x875Q0909144S \xf1\x891063\xf1\x82\00516B00501A1',
      b'\xf1\x875Q0909144T \xf1\x891072\xf1\x82\00521B00703A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x873Q0907572B \xf1\x890192',
      b'\xf1\x873Q0907572C \xf1\x890195',
      b'\xf1\x875Q0907572R \xf1\x890771',
    ],
  },
  CAR.TIGUAN_MK2: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8783A907115B \xf1\x890005',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x8709G927158DT\xf1\x893698',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655BM\xf1\x890403\xf1\x82\02316143231313500314641011750179333423100',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875QM909144C \xf1\x891082\xf1\x82\00521A60804A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x872Q0907572R \xf1\x890372',
    ],
  },
  CAR.AUDI_A3_MK3: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906023AN\xf1\x893695',
      b'\xf1\x8704E906023AR\xf1\x893440',
      b'\xf1\x8704E906023BL\xf1\x895190',
      b'\xf1\x8704L997022N \xf1\x899459',
      b'\xf1\x875G0906259L \xf1\x890002',
      b'\xf1\x878V0906264B \xf1\x890003',
      b'\xf1\x878V0907115B \xf1\x890007',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870CW300048  \xf1\x895201',
      b'\xf1\x870D9300013B \xf1\x894931',
      b'\xf1\x870D9300041N \xf1\x894512',
      b'\xf1\x870DD300046A \xf1\x891602',
      b'\xf1\x870DD300046F \xf1\x891602',
      b'\xf1\x870DD300046G \xf1\x891601',
      b'\xf1\x870GC300042J \xf1\x891402',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655AM\xf1\x890315\xf1\x82\x1311111111111111311411011231129321212100',
      b'\xf1\x875Q0959655J \xf1\x890825\xf1\x82\023111112111111--171115141112221291163221',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\023121111111211--261117141112231291163221',
      b'\xf1\x875Q0959655J \xf1\x890830\xf1\x82\x13121111111111--341117141212231291163221',
      b'\xf1\x875Q0959655N \xf1\x890361\xf1\x82\0211212001112111104110411111521159114',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909144P \xf1\x891043\xf1\x82\00503G00803A0',
      b'\xf1\x875Q0909144R \xf1\x891061\xf1\x82\00516G00804A1',
      b'\xf1\x875Q0909144T \xf1\x891072\xf1\x82\00521G00807A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572D \xf1\x890304\xf1\x82\00101',
      b'\xf1\x875Q0907572G \xf1\x890571',
    ],
  },
  CAR.SEAT_ATECA_MK1: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906027KA\xf1\x893749',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870D9300014S \xf1\x895202',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x873Q0959655BH\xf1\x890703\xf1\x82\0161212001211001305121211052900',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x873Q0909144L \xf1\x895081\xf1\x82\00571N60511A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x872Q0907572M \xf1\x890233',
    ],
  },
  CAR.SKODA_KODIAQ_MK1: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906027DD\xf1\x893123',
      b'\xf1\x875NA907115E \xf1\x890003',
      b'\xf1\x8704L906026DE\xf1\x895418',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870D9300043  \xf1\x895202',
      b'\xf1\x870DL300012M \xf1\x892107',
      b'\xf1\x870DL300012N \xf1\x892110',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x873Q0959655BJ\xf1\x890703\xf1\x82\0161213001211001205212111052100',
      b'\xf1\x873Q0959655CQ\xf1\x890720\xf1\x82\x0e1213111211001205212112052111',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909143P \xf1\x892051\xf1\x820527T6050405',
      b'\xf1\x875Q0909143P \xf1\x892051\xf1\x820527T6060405',
      b'\xf1\x875Q0910143C \xf1\x892211\xf1\x82\x0567T600G600',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x872Q0907572R \xf1\x890372',
      b'\xf1\x872Q0907572Q \xf1\x890342',
    ],
  },
  CAR.SKODA_OCTAVIA_MK3: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704E906027HD\xf1\x893742',
      b'\xf1\x8704L906021DT\xf1\x898127',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870CW300043B \xf1\x891601',
      b'\xf1\x870D9300041P \xf1\x894507',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x873Q0959655AC\xf1\x890200\xf1\x82\r11120011100010022212110200',
      b'\xf1\x873Q0959655CN\xf1\x890720\xf1\x82\x0e3221003221002105755331052100',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909144AB\xf1\x891082\xf1\x82\x0521T00403A1',
      b'\xf1\x875Q0909144R \xf1\x891061\xf1\x82\x0516A00604A1',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x875Q0907572D \xf1\x890304\xf1\x82\x0101',
      b'\xf1\x875Q0907572P \xf1\x890682',
    ],
  },
  CAR.SKODA_SCALA_MK1: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704C906025AK\xf1\x897053',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870CW300050  \xf1\x891709',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x872Q0959655AM\xf1\x890351\xf1\x82\022111104111104112104040404111111112H14',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x872Q1909144M \xf1\x896041',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x872Q0907572R \xf1\x890372',
    ],
  },
  CAR.SKODA_SUPERB_MK3: {
    (Ecu.engine, 0x7e0, None): [
      b'\xf1\x8704L906026KB\xf1\x894071',
      b'\xf1\x873G0906259B \xf1\x890002',
      b'\xf1\x8704L906026FP\xf1\x891196',
    ],
    (Ecu.transmission, 0x7e1, None): [
      b'\xf1\x870D9300012  \xf1\x894940',
      b'\xf1\x870D9300011T \xf1\x894801',
    ],
    (Ecu.srs, 0x715, None): [
      b'\xf1\x875Q0959655AE\xf1\x890130\xf1\x82\022111200111121001121118112231292221111',
      b'\xf1\x875Q0959655BH\xf1\x890336\xf1\x82\02331310031313100313131013141319331413100',
      b'\xf1\x875Q0959655AK\xf1\x890130\xf1\x82\022111200111121001121110012211292221111',
    ],
    (Ecu.eps, 0x712, None): [
      b'\xf1\x875Q0909143M \xf1\x892041\xf1\x820522UZ070303',
      b'\xf1\x875Q0910143B \xf1\x892201\xf1\x82\00563UZ060700',
      b'\xf1\x875Q0909143K \xf1\x892033\xf1\x820514UZ070203',
    ],
    (Ecu.fwdRadar, 0x757, None): [
      b'\xf1\x873Q0907572B \xf1\x890194',
      b'\xf1\x873Q0907572C \xf1\x890195',
      b'\xf1\x873Q0907572B \xf1\x890192',
    ],
  },
}

DBC = {
  CAR.ATLAS_MK1: dbc_dict('vw_mqb_2010', None),
  CAR.GOLF_MK7: dbc_dict('vw_mqb_2010', None),
  CAR.JETTA_MK7: dbc_dict('vw_mqb_2010', None),
  CAR.PASSAT_MK8: dbc_dict('vw_mqb_2010', None),
  CAR.TIGUAN_MK2: dbc_dict('vw_mqb_2010', None),
  CAR.AUDI_A3_MK3: dbc_dict('vw_mqb_2010', None),
  CAR.SEAT_ATECA_MK1: dbc_dict('vw_mqb_2010', None),
  CAR.SKODA_KODIAQ_MK1: dbc_dict('vw_mqb_2010', None),
  CAR.SKODA_OCTAVIA_MK3: dbc_dict('vw_mqb_2010', None),
  CAR.SKODA_SCALA_MK1: dbc_dict('vw_mqb_2010', None),
  CAR.SKODA_SUPERB_MK3: dbc_dict('vw_mqb_2010', None),
}
