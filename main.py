from dataclasses import dataclass
from statistics import mean

@dataclass
class Student:
    name: str
    age: int
    grades: list[float]

    @property
    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return mean(self.grades)
```

Kodni ishlatish uchun misol:

```python
student = Student("Ali", 20, [90, 80, 95])
print(student.average_grade)  # 88.33333333333333
