num1=98
class InvalidScoreError(Exception):
    pass


def validate_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError("คะแนนต้องอยู่ระหว่าง 0-100")

    return score


try:
    score = validate_score(num1)

except InvalidScoreError as error:
    print(f"คะแนนไม่ถูกต้อง: {error}")