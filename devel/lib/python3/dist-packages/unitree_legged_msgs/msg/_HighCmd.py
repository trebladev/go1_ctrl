# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from unitree_legged_msgs/HighCmd.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import unitree_legged_msgs.msg

class HighCmd(genpy.Message):
  _md5sum = "662e986e0a4446722bb9fac50f5d8cfd"
  _type = "unitree_legged_msgs/HighCmd"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 levelFlag
uint16 commVersion              # Old version Aliengo does not have
uint16 robotID                  # Old version Aliengo does not have
uint32 SN                       # Old version Aliengo does not have
uint8 bandWidth                 # Old version Aliengo does not have
uint8 mode                      # 0. idle, default stand  
                                # 1. force stand (controlled by dBodyHeight + ypr)
                                # 2. target velocity walking (controlled by velocity + yawSpeed)
                                # 3. target position walking (controlled by position + ypr[0])
                                # 4. path mode walking (reserve for future release)
                                # 5. position stand down. 
                                # 6. position stand up 
                                # 7. damping mode 
                                # 8. recovery stand
                                # 9. backflip
                                # 10. jumpYaw
                                # 11. straightHand
                                # 12. dance1
                                # 13. dance2
                                # 14. two leg stand
uint8 gaitType                  # 0.idle  1.trot  2.trot running  3.climb stair
uint8 speedLevel                # 0. default low speed. 1. medium speed 2. high speed. during walking, only respond MODE 3
float32 footRaiseHeight         # (unit: m, default: 0.08m), foot up height while walking
float32 bodyHeight              # (unit: m, default: 0.28m),
float32[2] postion              # (unit: m), desired position in inertial frame
float32[3] euler                # (unit: rad), roll pitch yaw in stand mode
float32[2] velocity             # (unit: m/s), forwardSpeed, sideSpeed in body frame
float32 yawSpeed                # (unit: rad/s), rotateSpeed in body frame
BmsCmd bms
LED[4] led
uint8[40] wirelessRemote
uint32 reserve                  # Old version Aliengo does not have
int32 crc
================================================================================
MSG: unitree_legged_msgs/BmsCmd
uint8 off            # off 0xA5
uint8[3] reserve
================================================================================
MSG: unitree_legged_msgs/LED
uint8 r
uint8 g
uint8 b"""
  __slots__ = ['levelFlag','commVersion','robotID','SN','bandWidth','mode','gaitType','speedLevel','footRaiseHeight','bodyHeight','postion','euler','velocity','yawSpeed','bms','led','wirelessRemote','reserve','crc']
  _slot_types = ['uint8','uint16','uint16','uint32','uint8','uint8','uint8','uint8','float32','float32','float32[2]','float32[3]','float32[2]','float32','unitree_legged_msgs/BmsCmd','unitree_legged_msgs/LED[4]','uint8[40]','uint32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       levelFlag,commVersion,robotID,SN,bandWidth,mode,gaitType,speedLevel,footRaiseHeight,bodyHeight,postion,euler,velocity,yawSpeed,bms,led,wirelessRemote,reserve,crc

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HighCmd, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.levelFlag is None:
        self.levelFlag = 0
      if self.commVersion is None:
        self.commVersion = 0
      if self.robotID is None:
        self.robotID = 0
      if self.SN is None:
        self.SN = 0
      if self.bandWidth is None:
        self.bandWidth = 0
      if self.mode is None:
        self.mode = 0
      if self.gaitType is None:
        self.gaitType = 0
      if self.speedLevel is None:
        self.speedLevel = 0
      if self.footRaiseHeight is None:
        self.footRaiseHeight = 0.
      if self.bodyHeight is None:
        self.bodyHeight = 0.
      if self.postion is None:
        self.postion = [0.] * 2
      if self.euler is None:
        self.euler = [0.] * 3
      if self.velocity is None:
        self.velocity = [0.] * 2
      if self.yawSpeed is None:
        self.yawSpeed = 0.
      if self.bms is None:
        self.bms = unitree_legged_msgs.msg.BmsCmd()
      if self.led is None:
        self.led = [unitree_legged_msgs.msg.LED() for _ in range(4)]
      if self.wirelessRemote is None:
        self.wirelessRemote = b'\0'*40
      if self.reserve is None:
        self.reserve = 0
      if self.crc is None:
        self.crc = 0
    else:
      self.levelFlag = 0
      self.commVersion = 0
      self.robotID = 0
      self.SN = 0
      self.bandWidth = 0
      self.mode = 0
      self.gaitType = 0
      self.speedLevel = 0
      self.footRaiseHeight = 0.
      self.bodyHeight = 0.
      self.postion = [0.] * 2
      self.euler = [0.] * 3
      self.velocity = [0.] * 2
      self.yawSpeed = 0.
      self.bms = unitree_legged_msgs.msg.BmsCmd()
      self.led = [unitree_legged_msgs.msg.LED() for _ in range(4)]
      self.wirelessRemote = b'\0'*40
      self.reserve = 0
      self.crc = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B2HI4B2f().pack(_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth, _x.mode, _x.gaitType, _x.speedLevel, _x.footRaiseHeight, _x.bodyHeight))
      buff.write(_get_struct_2f().pack(*self.postion))
      buff.write(_get_struct_3f().pack(*self.euler))
      buff.write(_get_struct_2f().pack(*self.velocity))
      _x = self
      buff.write(_get_struct_fB().pack(_x.yawSpeed, _x.bms.off))
      _x = self.bms.reserve
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_3B().pack(*_x))
      else:
        buff.write(_get_struct_3s().pack(_x))
      if len(self.led) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.led), 'self.led')))
      for val1 in self.led:
        _x = val1
        buff.write(_get_struct_3B().pack(_x.r, _x.g, _x.b))
      _x = self.wirelessRemote
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_40B().pack(*_x))
      else:
        buff.write(_get_struct_40s().pack(_x))
      _x = self
      buff.write(_get_struct_Ii().pack(_x.reserve, _x.crc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bms is None:
        self.bms = unitree_legged_msgs.msg.BmsCmd()
      if self.led is None:
        self.led = None
      end = 0
      _x = self
      start = end
      end += 21
      (_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth, _x.mode, _x.gaitType, _x.speedLevel, _x.footRaiseHeight, _x.bodyHeight,) = _get_struct_B2HI4B2f().unpack(str[start:end])
      start = end
      end += 8
      self.postion = _get_struct_2f().unpack(str[start:end])
      start = end
      end += 12
      self.euler = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 8
      self.velocity = _get_struct_2f().unpack(str[start:end])
      _x = self
      start = end
      end += 5
      (_x.yawSpeed, _x.bms.off,) = _get_struct_fB().unpack(str[start:end])
      start = end
      end += 3
      self.bms.reserve = str[start:end]
      self.led = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.LED()
        _x = val1
        start = end
        end += 3
        (_x.r, _x.g, _x.b,) = _get_struct_3B().unpack(str[start:end])
        self.led.append(val1)
      start = end
      end += 40
      self.wirelessRemote = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.reserve, _x.crc,) = _get_struct_Ii().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B2HI4B2f().pack(_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth, _x.mode, _x.gaitType, _x.speedLevel, _x.footRaiseHeight, _x.bodyHeight))
      buff.write(self.postion.tostring())
      buff.write(self.euler.tostring())
      buff.write(self.velocity.tostring())
      _x = self
      buff.write(_get_struct_fB().pack(_x.yawSpeed, _x.bms.off))
      _x = self.bms.reserve
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_3B().pack(*_x))
      else:
        buff.write(_get_struct_3s().pack(_x))
      if len(self.led) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.led), 'self.led')))
      for val1 in self.led:
        _x = val1
        buff.write(_get_struct_3B().pack(_x.r, _x.g, _x.b))
      _x = self.wirelessRemote
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(_get_struct_40B().pack(*_x))
      else:
        buff.write(_get_struct_40s().pack(_x))
      _x = self
      buff.write(_get_struct_Ii().pack(_x.reserve, _x.crc))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bms is None:
        self.bms = unitree_legged_msgs.msg.BmsCmd()
      if self.led is None:
        self.led = None
      end = 0
      _x = self
      start = end
      end += 21
      (_x.levelFlag, _x.commVersion, _x.robotID, _x.SN, _x.bandWidth, _x.mode, _x.gaitType, _x.speedLevel, _x.footRaiseHeight, _x.bodyHeight,) = _get_struct_B2HI4B2f().unpack(str[start:end])
      start = end
      end += 8
      self.postion = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
      start = end
      end += 12
      self.euler = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 8
      self.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
      _x = self
      start = end
      end += 5
      (_x.yawSpeed, _x.bms.off,) = _get_struct_fB().unpack(str[start:end])
      start = end
      end += 3
      self.bms.reserve = str[start:end]
      self.led = []
      for i in range(0, 4):
        val1 = unitree_legged_msgs.msg.LED()
        _x = val1
        start = end
        end += 3
        (_x.r, _x.g, _x.b,) = _get_struct_3B().unpack(str[start:end])
        self.led.append(val1)
      start = end
      end += 40
      self.wirelessRemote = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.reserve, _x.crc,) = _get_struct_Ii().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_3B = None
def _get_struct_3B():
    global _struct_3B
    if _struct_3B is None:
        _struct_3B = struct.Struct("<3B")
    return _struct_3B
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_3s = None
def _get_struct_3s():
    global _struct_3s
    if _struct_3s is None:
        _struct_3s = struct.Struct("<3s")
    return _struct_3s
_struct_40B = None
def _get_struct_40B():
    global _struct_40B
    if _struct_40B is None:
        _struct_40B = struct.Struct("<40B")
    return _struct_40B
_struct_40s = None
def _get_struct_40s():
    global _struct_40s
    if _struct_40s is None:
        _struct_40s = struct.Struct("<40s")
    return _struct_40s
_struct_B2HI4B2f = None
def _get_struct_B2HI4B2f():
    global _struct_B2HI4B2f
    if _struct_B2HI4B2f is None:
        _struct_B2HI4B2f = struct.Struct("<B2HI4B2f")
    return _struct_B2HI4B2f
_struct_Ii = None
def _get_struct_Ii():
    global _struct_Ii
    if _struct_Ii is None:
        _struct_Ii = struct.Struct("<Ii")
    return _struct_Ii
_struct_fB = None
def _get_struct_fB():
    global _struct_fB
    if _struct_fB is None:
        _struct_fB = struct.Struct("<fB")
    return _struct_fB
