def reward_function(params):
  '''
  Example of rewarding the agent to follow center line
  '''

  track_width = params['track_width']
  distance_from_center = params['distance_from_center']

  marker_1 = 0.1*track_width
  marker_2 = 0.25*track_width
  marker_3 = 0.5*track_width
  if distance_from_center ≤ marker_1:
    reward = 1
  elif distance_from_center ≤ marker_2:
    reward = 0.5
  elif distance_from_center ≤ marker_3:
    reward = 0.1
  else:
    reward = 1e-3 # likely crashed/ close to off track
  return reward

def reward_function_2(params):
    reward = 0.001
    if params["all_wheels_on_track"]:
        reward += 1
    if abs(params["steering_angle"]) < 5:
       reward += 1
    reward += ( params["speed"] / 8 )
    return float(reward)
