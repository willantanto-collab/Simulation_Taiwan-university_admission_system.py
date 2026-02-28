#project : Taiwan University Overseas Admission Analysis Engine
#Purpose : 为华侨生申请台湾的大学提供精准的加权计算与录取模拟
#name: Harry
class IdentityValidator:
    def __init__(self, name, total_days, yearly_logs):
        self.name = name
        self.total_days = total_days
        self.yearly_logs = yearly_logs # 格式: {2021: 100, 2022: 30}
        self.is_legal = False
        self.error_code = None # 记录拒绝原因
    def validate(self):
        if self.total_days < 2190: #检查总时长，海外必须住满 6 年（2190天）
            self.error_code = "total_days_low" #总天数过低
            return False
        for year in self.yearly_logs:  # 检查每一年，回台湾探亲，旅游的时间，一年加起来不能超过 120 天
            if self.yearly_logs[year] > 120:
                self.error_code = f"stay_over_limit_{year}"
                return False
        self.is_legal = True
        self.error_code = "PASSED"
        return True
class Department:
  def __init__(self,name,threshold,code,score):
    self.name = name
    self.threshold = threshold
    self.code = code
    self.score = score
  def analyse_admission(self):
    margin = (self.score - self.threshold)/self.threshold #门槛，判断学生的成绩是否能进
    if margin >= 0.1: #超过10%
        return "稳定录取”
    elif margin >= 0: 
        return "录取概率高"
    else:
        return "存在风选，建议作为冲刺志向”
class AdmissionAnalyser:  #通用录取分析，确保逻辑链可扩展
  def __init__(self,grades):
    self.grades = grades
    self.num_subjects = totalsubjects
  def calculate_weighted_score(self): #通用台北大学可判断的统一成绩，含金量之类的
    #实现具体的加权计算
    pass
class Cambridge_Analyser(AdmissionAnalyser):  #具体cambridge 的
  def calculate_weighted_score(self):
    if len(self.grades) != self.num_subjects: #确认考生成绩个数和科目数量是否对的上
      return "错误：填入成绩数与声明科目数不符”
    actual_total = sum(self.grades)
    average_score = actual_total /self.num_subjects
    diffciulty_weight = 1.05 #每年可更改，不同的含金量系数
    unified_score = average_score * difficulty_weight #通用台北大学判断的统一成绩
    return unified_score
class TaiwanUni_CSIE_Alevel_System(Department): #针对A level,3核心科目体系的质工系录取模拟
  def __init__(self,student_name,grades):
    self.student_name = student_name
    self.weights = {"Math":2.2,"CS":2.0,"Physics":1.8} #设定质工系特定权重
    analyser = Cambridge_Analyser(student_grades)
    final_score = analyser.calculate_weighted_score()
    super().__init__(name="台湾的大学质工系”，threshold=310,code = "CSIE",score=final_score) #继承
class GrowthAnalyser: #成绩上的潜力和改变
  def __init__(self,junior_score,senior_score，potential_multiplier,activities):
    self.junior_score = junior_score
    self.senior_score = senior_score
    self.potential_multiplier = 1.0 #初始调整数据，潜力乘数
    self.activities = []
  def calculate_growth_rate(self):
    if self.junior_score <= 0: 
      return 0.0
    return (self.junior_score - self.senior_score)/self.senior_score
  def get_potential_status(self):
    rate = self.calculate_growth_rate()
    if rate >= 0.3: #如果进步超过30%就是强自驱力
      return "High Potential/Strong Self-Driven"
    elif rate >= 0.2 and rate < 0.3:
      return "Fast Learner"
    elif rate >= 0.1 and rate < 0.2:
      return "Consistent learner"
    elif rate >= 0 and rate < 0.1:
      return ”Stable Learner"
    else:# 如果没有进步潜力
      return "Ongoing Academic Adaptation"
  def add_activity(self,act_name,years,hours_per_week,is_team = False,is_leader = False):
    activity_data = {'name'：act_name,'years':years,'hours':hours_per_week,'is_team':is_team,'is_leader=is_leader}
    self.activities.append(activity_data)
  def calculate_additionalpoints_activities(self):
    if not self.activties:
      self.potential_multiplier = 1.0
      return self.potential_multiplier
    total_growth_index = 0 #总和成长指标
    for act in self.activities:
      if act in self.activities: 
        if act['years'] >= 3: #计算努力价值，在长期性
          persistence_factor = 1.5 
        else:
          persistence_factor = 1.0
        persistence_score = act['years'] * persistence_factor #计算该项活动的持久分
      if act['hours'] > 15: #intensity_score 投入强度
        intensity_score = 15 * 0.4
      else:
        intensity_score = act['hours'] * 0.4
      bonus_points = 0 
      if act['is_team']:
        bonus_points += 2.0 #团队协作的加点初始定义
        if act ['is_leader']:
          bonus_points += 3.0 #因为更有领导能力，加分更多
      #统计该活动的贡献价值
      activity_impact = persistence_score + intensity_score + bonus_points
      total_points += activity_impact
    if total_points > 25:
      maximum_points = 25 #防止溢出，该分数上线
    else:
      maximum_points = total_points
self.potential_multiplier = 1 + (limited_points / 100) * 0.6 
return round(self.potential_multiplier,3) #确保计算严谨，精确     
