# 设定变量
min_angle = 0.0       # 最小角度
max_angle = 45.0      # 最大角度
low_speed_factor = 0.3  # 低速区间的最大值 (0-0.3)
max_speed = 1.0         # 最大速度仍然不超过1
transition_angle = 10.0  # 低速区间的起点
saturation_angle = 30.0  # 饱和速度的角度

# 定义新的二次曲线映射函数，增加低速区范围
def quadratic_mapping(angle):
    """
    方程式：  
    1. 在 0 到 transition_angle 之间，速度为 0
    2. 在 transition_angle 到 saturation_angle 之间，速度缓慢增加 (映射到 0-0.3)
       公式: 
       speed = ((angle - transition_angle) ^ 2) / (saturation_angle - transition_angle) ^ 2 * low_speed_factor
    3. 在 saturation_angle 到 max_angle 之间，速度更快增加到 1
       公式: 
       speed = low_speed_factor + (max_speed - low_speed_factor) * (angle - saturation_angle) / (max_angle - saturation_angle)
    """
    angle = min(max(angle, -max_angle), max_angle)  # 限制角度范围在 -max_angle 到 max_angle
    sign = 1.0 if angle >= 0 else -1.0
    abs_angle = abs(angle)
    
    # 在 0 到 transition_angle 之间，速度为 0
    if abs_angle <= transition_angle:
        speed = 0.0
    # 在 transition_angle 到 saturation_angle 之间，速度缓慢增加 (映射到 0-0.3)
    elif abs_angle <= saturation_angle:
        speed = (abs_angle - transition_angle) ** 2 / (saturation_angle - transition_angle) ** 2 * low_speed_factor
    # 在 saturation_angle 到 max_angle 之间，速度更快增加到 1
    else:
        speed = low_speed_factor + (max_speed - low_speed_factor) * (abs_angle - saturation_angle) / (max_angle - saturation_angle)

    return sign * speed
