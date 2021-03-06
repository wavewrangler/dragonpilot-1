#!/usr/bin/env python3.7
import subprocess
from cereal import car
from common.params import Params
params = Params()

def is_online():
  try:
    return not subprocess.call(["ping", "-W", "4", "-c", "1", "117.28.245.92"])
  except ProcessLookupError:
    return False

def common_controller_ctrl(enabled, dragon_lat_ctrl, dragon_enable_steering_on_signal, blinker_on, steer_req):
  if enabled:
    if (dragon_enable_steering_on_signal and blinker_on) or not dragon_lat_ctrl:
      steer_req = 0 if isinstance(steer_req, int) else False
  return steer_req

def common_interface_atl(ret, atl):
  # dp
  enable_acc = ret.cruiseState.enabled
  if atl and ret.cruiseState.available:
    enable_acc = True
    if ret.gearShifter in [car.CarState.GearShifter.reverse, car.CarState.GearShifter.park]:
      enable_acc = False
    if ret.seatbeltUnlatched or ret.doorOpen:
      enable_acc = False
  return enable_acc
