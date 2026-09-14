raw_records = [
    ("E101", "Aman", "Engineering", (85, 92, 88), ["Python", "SQL", "Git"]),
    ("E102", "Priya", "Marketing", (72, 68, 75), ["SEO", "Content"]),
    ("E103", "Rahul", "Engineering", (95, 90, 94), ["C", "Python", "Docker", "Linux"]),
    ("E104", "Simran", "HR", (60, 58, 62), ["Recruitment"]),
    ("E105", "Karan", "Marketing", (80, 85, 82), ["SEO", "Analytics", "Ads"]),
]

mandatory_skills = {"Python", "SQL"}
department_logs = {}
final_appraisals = {}
promoted_candidates = set()

for emp_id, name, dept, scores, skills in raw_records:
    avg_score = sum(scores) / len(scores) if len(scores) > 0 else 0
    skill_set = set(skills)
    
    meets_skill_req = mandatory_skills.issubset(skill_set) if dept == "Engineering" else len(skill_set) >= 2
    bonus_eligible = True if avg_score >= 80 and meets_skill_req else False
    rating = "Exceeds" if avg_score >= 88 else ("Meets" if avg_score >= 70 else "Needs Improvement")
    
    if bonus_eligible:
        promoted_candidates.add(name)
        
    final_appraisals[emp_id] = {
        "name": name,
        "dept": dept,
        "average": round(avg_score, 1),
        "rating": rating,
        "bonus": 1500 if bonus_eligible else 500,
        "skill_count": len(skill_set)
    }
    
    dept_entry = department_logs.get(dept, [])
    dept_entry.append(avg_score)
    department_logs[dept] = dept_entry

dept_averages = {
    dept: round(sum(scores_list) / len(scores_list), 2)
    for dept, scores_list in department_logs.items()
}

top_employee = max(
    final_appraisals.items(),
    key=lambda item: item[1]["average"]
)[1]["name"] if final_appraisals else "None"

print("EMPLOYEE APPRAISALS:")
for eid, record in final_appraisals.items():
    print(eid, record)

print("\nDEPARTMENT BENCHMARKS:")
for dept, avg in dept_averages.items():
    status = "Target Met" if avg >= 75.0 else "Target Missed"
    print(f"{dept}: {avg} -> {status}")

print("\nBONUS AWARDEES:")
print(promoted_candidates)

print("\nTOP PERFORMER:")
print(top_employee)