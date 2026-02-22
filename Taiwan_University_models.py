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
