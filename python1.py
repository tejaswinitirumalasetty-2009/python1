1. University Scholarship Allocation
Problem Statement
Evaluate applicants using aggregate marks, subject-wise minimum marks, attendance and family income. Rank eligible applicants by aggregate marks; break ties using attendance.
Objectives
Identify eligible applicants and produce a merit ranking with deterministic tie-breaking.
Assumptions
Eligibility: aggregate ≥ 75, every subject ≥ 60, attendance ≥ 75%, and annual family income ≤ ₹250000.
Algorithm
1.	Start.
2.	Read each applicant's name, aggregate, subject marks, attendance and income.
3.	Check all four eligibility conditions.
4.	Store eligible applicants with aggregate and attendance.
5.	Sort by aggregate descending, then attendance descending.
6.	Display the ranked list and stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Parallelogram) Input applicant name, aggregate marks, subject marks, attendance and family income.
↓
3. (Diamond) Are all conditions satisfied: aggregate ≥ 75, every subject ≥ 60, attendance ≥ 75%, and income ≤ ₹250000?
   ├── NO → (Rectangle) Skip this applicant.
   └── YES → (Rectangle) Add applicant to the eligible list.
↓
4. (Decision/Loop) Are there more applicants?
   ├── YES → Return to Step 2.
   └── NO → Continue.
↓
5. (Rectangle) Sort eligible applicants by aggregate marks in descending order; use attendance to break ties.
↓
6. (Parallelogram) Display the scholarship merit list.
↓
7. (Oval) END
Python Source Code
applicants = [
    ("Asha", 88, [90, 82, 91], 92, 200000),
    ("Bala", 88, [80, 65, 85], 85, 220000),
    ("Charan", 72, [75, 80, 70], 90, 180000),
    ("Divya", 91, [95, 89, 92], 80, 240000)
]

eligible = []
for name, aggregate, subjects, attendance, income in applicants:
    if (aggregate >= 75 and min(subjects) >= 60
            and attendance >= 75 and income <= 250000):
        eligible.append((name, aggregate, attendance))

eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)
print("Scholarship Merit List")
for rank, student in enumerate(eligible, 1):
    print(rank, student[0], "Aggregate:", student[1],
          "Attendance:", str(student[2]) + "%")
Sample Output
Scholarship Merit List
1 Divya Aggregate: 91 Attendance: 80%
2 Asha Aggregate: 88 Attendance: 92%
3 Bala Aggregate: 88 Attendance: 85%
Conclusion
The program filters applicants according to the stated rules and ranks eligible students. Asha ranks above Bala because their aggregate marks tie but Asha has higher attendance.
 
2. Progressive Electricity Billing
Problem Statement
Calculate a household's electricity bill using consumption slabs, fixed charge, surcharge and rebate; compare three months of consumption.
Objectives
Calculate slab-wise charges and identify the month with the highest bill.
Assumptions
First 100 units cost ₹2/unit; next 100 cost ₹3/unit; units above 200 cost ₹5/unit. Fixed charge ₹50. Add 5% surcharge when energy charge exceeds ₹500; give ₹20 rebate when consumption is below 100 units.
Algorithm
7.	Start.
8.	Read monthly units.
9.	Calculate energy charge by applying each slab.
10.	Add fixed charge.
11.	Apply surcharge and rebate conditions.
12.	Print each bill and identify the highest bill.
13.	Stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Input/Output) Read the electricity units used for each month.
↓
3. (Diamond) Are units ≤ 100?
   ├── YES → (Rectangle) Energy charge = units × ₹2.
   └── NO → Check the next condition.
↓
4. (Diamond) Are units ≤ 200?
   ├── YES → (Rectangle) Energy charge = ₹200 + (units − 100) × ₹3.
   └── NO → (Rectangle) Energy charge = ₹200 + ₹300 + (units − 200) × ₹5.
↓
5. (Rectangle) Add the fixed charge of ₹50 to the energy charge.
↓
6. (Diamond) Is the energy charge greater than ₹500? YES → Add 5% surcharge. NO → Skip surcharge.
↓
7. (Diamond) Are units below 100? YES → Subtract ₹20 rebate. NO → Skip rebate.
↓
8. (Parallelogram) Display the monthly bill and store it.
↓
9. (Diamond) Are more months left? YES → Return to Step 2. NO → Continue.
↓
10. (Rectangle) Find the month with the highest bill.
↓
11. (Parallelogram) Display the highest-bill month.
↓
12. (Oval) END
Python Source Code
months = ["June", "July", "August"]
usage = [80, 160, 260]
bills = []

for i in range(len(usage)):
    units = usage[i]
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = energy + 50
    if energy > 500:
        bill += energy * 0.05
    if units < 100:
        bill -= 20
    bills.append(bill)
    print(months[i], "Units:", units, "Bill: Rs.", round(bill, 2))

highest = bills.index(max(bills))
print("Highest bill:", months[highest])
Sample Output
June Units: 80 Bill: Rs. 190
July Units: 160 Bill: Rs. 430
August Units: 260 Bill: Rs. 945.0
Highest bill: August
Conclusion
The program calculates monthly bills using progressive slabs and conditional adjustments, then identifies the month with the highest bill.
 
3. Hospital Billing and Patient Classification
Problem Statement
Calculate consultation, diagnostic and treatment charges, apply a concession where eligible and classify the patient's payment category.
Objectives
Generate a final hospital bill and classify the amount payable.
Assumptions
A 10% concession applies if the patient is a senior citizen (age ≥ 60). Classify final bills below ₹1000 as Basic, ₹1000–₹5000 as Standard, and above ₹5000 as High.
Algorithm
14.	Start.
15.	Read patient age and three charge amounts.
16.	Add charges to find subtotal.
17.	If age is at least 60, calculate a 10% concession.
18.	Subtract concession and classify the final amount.
19.	Display the bill and stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Parallelogram) Input patient age, consultation charge, diagnostic charge and treatment charge.
↓
3. (Rectangle) Add the three charges to calculate the subtotal.
↓
4. (Diamond) Is the patient age ≥ 60?
   ├── YES → (Rectangle) Concession = 10% of subtotal.
   └── NO → (Rectangle) Concession = ₹0.
↓
5. (Rectangle) Final bill = subtotal − concession.
↓
6. (Diamond) Is final bill < ₹1000? YES → Category = Basic. NO → Continue.
↓
7. (Diamond) Is final bill ≤ ₹5000? YES → Category = Standard. NO → Category = High.
↓
8. (Parallelogram) Display subtotal, concession, final bill and patient category.
↓
9. (Oval) END
Python Source Code
age = 65
consultation = 500
diagnostics = 1200
treatment = 1800

subtotal = consultation + diagnostics + treatment
discount = subtotal * 0.10 if age >= 60 else 0
final_bill = subtotal - discount

if final_bill < 1000:
    category = "Basic"
elif final_bill <= 5000:
    category = "Standard"
else:
    category = "High"

print("Subtotal: Rs.", subtotal)
print("Concession: Rs.", round(discount, 2))
print("Final bill: Rs.", round(final_bill, 2))
print("Patient category:", category)
Sample Output
Subtotal: Rs. 3500
Concession: Rs. 350.0
Final bill: Rs. 3150.0
Patient category: Standard
Conclusion
The program totals hospital charges, applies the age-based concession and assigns the patient to the specified billing category.
 
4. Employee Payroll and Deduction Analysis
Problem Statement
Calculate gross salary from basic pay, allowances, overtime and incentives, then apply deductions and print a salary statement.
Objectives
Determine gross salary, deductions and net salary.
Assumptions
HRA is 20% of basic pay; allowance is ₹2000; overtime pay is ₹300/hour; incentive is ₹1500. Deduction is 5% of gross salary when gross salary is above ₹30000, otherwise 2%.
Algorithm
20.	Start.
21.	Read basic pay and overtime hours.
22.	Calculate HRA, overtime pay, allowance and incentive.
23.	Add them to basic pay to get gross salary.
24.	Calculate deduction based on gross salary.
25.	Subtract deduction to get net salary and display the statement.
26.	Stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Parallelogram) Input basic pay and overtime hours.
↓
3. (Rectangle) Calculate HRA = 20% of basic pay; allowance = ₹2000; overtime = hours × ₹300; incentive = ₹1500.
↓
4. (Rectangle) Gross salary = basic pay + HRA + allowance + overtime + incentive.
↓
5. (Diamond) Is gross salary > ₹30000?
   ├── YES → (Rectangle) Deduction = 5% of gross salary.
   └── NO → (Rectangle) Deduction = 2% of gross salary.
↓
6. (Rectangle) Net salary = gross salary − deduction.
↓
7. (Parallelogram) Display basic pay, gross salary, deduction and net salary.
↓
8. (Oval) END
Python Source Code
basic = 25000
overtime_hours = 5
hra = basic * 0.20
allowance = 2000
overtime = overtime_hours * 300
incentive = 1500

gross = basic + hra + allowance + overtime + incentive
rate = 0.05 if gross > 30000 else 0.02
deduction = gross * rate
net = gross - deduction

print("Basic pay: Rs.", basic)
print("Gross salary: Rs.", round(gross, 2))
print("Deduction: Rs.", round(deduction, 2))
print("Net salary: Rs.", round(net, 2))
Sample Output
Basic pay: Rs. 25000
Gross salary: Rs. 35000.0
Deduction: Rs. 1750.0
Net salary: Rs. 33250.0
Conclusion
The program calculates gross and net salary by combining pay components and applying a conditional deduction.
 
5. Multi-Plan Telecommunications Cost Optimization
Problem Statement
Compare mobile plans based on included data, monthly price, extra usage charges and a user's budget.
Objectives
Choose the least expensive plan that meets usage and budget requirements.
Assumptions
Plan A: ₹199 includes 2 GB, extra data ₹50/GB. Plan B: ₹299 includes 5 GB, extra ₹40/GB. Plan C: ₹399 includes 10 GB, extra ₹30/GB. Usage is 6 GB and budget is ₹400.
Algorithm
27.	Start.
28.	Store each plan's price, included data and excess rate.
29.	For each plan, calculate excess data and total cost.
30.	Keep plans that cost within budget.
31.	Choose the least expensive eligible plan.
32.	Display all costs and the best plan; stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Rectangle/Input) Set the mobile plans, usage = 6 GB and budget = ₹400.
↓
3. (Rectangle) For each plan, calculate extra data = max(0, usage − included data).
↓
4. (Rectangle) Calculate total plan cost = monthly price + extra data × extra-data rate.
↓
5. (Parallelogram) Display the total cost for the current plan.
↓
6. (Diamond) Is plan cost ≤ ₹400?
   ├── YES → (Rectangle) Add the plan and its cost to the eligible list.
   └── NO → Do not add the plan.
↓
7. (Diamond/Loop) Are more plans left? YES → Return to Step 3. NO → Continue.
↓
8. (Diamond) Is the eligible list empty?
   ├── YES → (Parallelogram) Display “No plan fits the budget.”
   └── NO → (Rectangle) Select the eligible plan with the lowest cost; display the best plan.
↓
9. (Oval) END
Python Source Code
plans = [
    ("Plan A", 199, 2, 50),
    ("Plan B", 299, 5, 40),
    ("Plan C", 399, 10, 30)
]
usage = 6
budget = 400
eligible = []

for name, price, included, extra_rate in plans:
    extra = max(0, usage - included)
    cost = price + extra * extra_rate
    print(name, "total cost: Rs.", cost)
    if cost <= budget:
        eligible.append((cost, name))

if eligible:
    best = min(eligible)
    print("Best plan:", best[1], "Cost: Rs.", best[0])
else:
    print("No plan fits the budget.")
Sample Output
Plan A total cost: Rs. 399
Plan B total cost: Rs. 339
Plan C total cost: Rs. 399
Best plan: Plan B Cost: Rs. 339
Conclusion
The program compares plan costs for a given usage level and selects the lowest-cost option within the budget.
 
6. Railway Fare and Reservation Calculator
Problem Statement
Calculate railway fares for passengers based on distance, class, age concession and reservation fees.
Objectives
Calculate individual fares and the total booking amount.
Assumptions
Base fare is ₹1.50/km for Sleeper and ₹3/km for AC. Reservation fee is ₹40 per passenger. Passengers aged 60 or above receive a 40% concession on base fare only.
Algorithm
33.	Start.
34.	Read distance, class and passenger ages.
35.	Choose the base rate according to class.
36.	Calculate base fare for each passenger.
37.	Apply senior concession where applicable and add reservation fee.
38.	Print each passenger fare and total; stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Parallelogram) Input travel distance, travel class and passenger ages.
↓
3. (Diamond) Is travel class AC?
   ├── YES → (Rectangle) Rate = ₹3 per km.
   └── NO → (Rectangle) Rate = ₹1.50 per km (Sleeper).
↓
4. (Rectangle) For each passenger, calculate base fare = distance × rate.
↓
5. (Diamond) Is passenger age ≥ 60?
   ├── YES → (Rectangle) Apply 40% concession to base fare (pay 60% of base fare).
   └── NO → Keep the full base fare.
↓
6. (Rectangle) Passenger fare = adjusted base fare + ₹40 reservation fee.
↓
7. (Rectangle) Add passenger fare to the total booking fare.
↓
8. (Parallelogram) Display this passenger’s fare.
↓
9. (Diamond/Loop) Are more passengers left? YES → Return to Step 4. NO → Continue.
↓
10. (Parallelogram) Display the total booking fare.
↓
11. (Oval) END
Python Source Code
distance = 300
travel_class = "AC"
ages = [22, 65, 40]
rate = 3 if travel_class == "AC" else 1.5
reservation_fee = 40
total = 0

for age in ages:
    base_fare = distance * rate
    if age >= 60:
        base_fare *= 0.60
    fare = base_fare + reservation_fee
    total += fare
    print("Age:", age, "Fare: Rs.", round(fare, 2))

print("Total booking fare: Rs.", round(total, 2))
Sample Output
Age: 22 Fare: Rs. 940
Age: 65 Fare: Rs. 580.0
Age: 40 Fare: Rs. 940
Total booking fare: Rs. 2460.0
Conclusion
The program computes passenger-wise fares, applies a senior concession to the base fare and adds reservation fees.
 
7. Retail Billing with Multiple Discount Rules
Problem Statement
Calculate an itemized retail bill with quantities, category taxes and a discount for purchases above a threshold.
Objectives
Find the subtotal, discount, tax and final amount.
Assumptions
Products have price and category-specific tax rates. A 10% discount applies when subtotal is at least ₹2000, capped at ₹300. Tax is calculated on the discounted value.
Algorithm
39.	Start.
40.	Read/store products, quantities, prices and tax rates.
41.	Calculate each line amount and subtotal.
42.	If subtotal ≥ ₹2000, calculate 10% discount capped at ₹300.
43.	Calculate tax on discounted line amounts using each category rate.
44.	Print item totals and final bill; stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Rectangle/Input) Read or set each product’s name, price, quantity and tax rate.
↓
3. (Rectangle) For each product, calculate amount = price × quantity and add it to subtotal.
↓
4. (Parallelogram) Display each product amount.
↓
5. (Diamond/Loop) Are more products left? YES → Return to Step 3. NO → Continue.
↓
6. (Diamond) Is subtotal ≥ ₹2000?
   ├── YES → (Rectangle) Discount = the smaller of 10% of subtotal or ₹300.
   └── NO → (Rectangle) Discount = ₹0.
↓
7. (Rectangle) Calculate the discounted-value factor = (subtotal − discount) ÷ subtotal (or 0 if subtotal is 0).
↓
8. (Rectangle) Calculate each product’s tax using its tax rate and the discounted value; add taxes.
↓
9. (Rectangle) Final amount = subtotal − discount + total tax.
↓
10. (Parallelogram) Display subtotal, discount, tax and final amount.
↓
11. (Oval) END
Python Source Code
products = [
    ("Shirt", 800, 2, 0.05),
    ("Bag", 1200, 1, 0.12)
]
subtotal = 0
tax_total = 0

for name, price, quantity, tax_rate in products:
    amount = price * quantity
    subtotal += amount
    print(name, "Amount: Rs.", amount)

discount = min(subtotal * 0.10, 300) if subtotal >= 2000 else 0
discount_factor = (subtotal - discount) / subtotal if subtotal else 0

for name, price, quantity, tax_rate in products:
    tax_total += price * quantity * discount_factor * tax_rate

final_amount = subtotal - discount + tax_total
print("Subtotal: Rs.", subtotal)
print("Discount: Rs.", round(discount, 2))
print("Tax: Rs.", round(tax_total, 2))
print("Final amount: Rs.", round(final_amount, 2))
Sample Output
Shirt Amount: Rs. 1600
Bag Amount: Rs. 1200
Subtotal: Rs. 2800
Discount: Rs. 280.0
Tax: Rs. 260.4
Final amount: Rs. 2780.4
Conclusion
The program generates a bill by calculating item amounts, applying the threshold discount and adding category-based tax.
 
8. Manufacturing Cost and Profitability Analysis
Problem Statement
Calculate total production cost including materials, labour, machine costs and wastage, then determine whether the profit target is met.
Objectives
Calculate cost per unit, revenue, profit and target status.
Assumptions
Material cost ₹5000, labour ₹2000, machine cost ₹1000 and wastage is 5% of material cost. Produce 100 units at a selling price of ₹100 each. Target profit is ₹1500.
Algorithm
45.	Start.
46.	Read/store cost components, quantity and selling price.
47.	Calculate wastage cost and total production cost.
48.	Calculate revenue and profit.
49.	Compare profit with the target.
50.	Display cost, revenue, profit and target status; stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Input/Output) Read or set material cost, labour cost, machine cost, quantity, selling price and target profit.
↓
3. (Rectangle) Wastage cost = 5% of material cost.
↓
4. (Rectangle) Total production cost = material + labour + machine + wastage.
↓
5. (Rectangle) Revenue = quantity × selling price.
↓
6. (Rectangle) Profit = revenue − total production cost.
↓
7. (Diamond) Is profit ≥ target profit?
   ├── YES → (Parallelogram) Display “Target achieved”.
   └── NO → (Parallelogram) Display “Target not achieved”.
↓
8. (Parallelogram) Display total cost, revenue and profit.
↓
9. (Oval) END
Python Source Code
material = 5000
labour = 2000
machine = 1000
wastage = material * 0.05
quantity = 100
selling_price = 100
target_profit = 1500

total_cost = material + labour + machine + wastage
revenue = quantity * selling_price
profit = revenue - total_cost

print("Total production cost: Rs.", total_cost)
print("Revenue: Rs.", revenue)
print("Profit: Rs.", profit)
if profit >= target_profit:
    print("Target achieved")
else:
    print("Target not achieved")
Sample Output
Total production cost: Rs. 8250.0
Revenue: Rs. 10000
Profit: Rs. 1750.0
Target achieved
Conclusion
The program includes wastage in production cost and checks whether the resulting profit reaches the target.
 
9. Multi-Currency Travel Budget Analysis
Problem Statement
Convert travel expenses from foreign currencies to rupees, add conversion fees and compare total spending with a budget.
Objectives
Calculate rupee expenses by category and identify the largest category.
Assumptions
Use supplied example rates: 1 USD = ₹83 and 1 EUR = ₹90. A 2% conversion fee is applied to each converted expense. These are illustrative rates, not live exchange rates.
Algorithm
51.	Start.
52.	Store each expense category, amount and currency rate.
53.	Convert each amount into rupees.
54.	Add a 2% conversion fee.
55.	Calculate total expenses and compare with budget.
56.	Find the largest expense category and display the report; stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Rectangle/Input) Read or set each expense category, foreign amount and conversion rate; set the budget.
↓
3. (Rectangle) For each expense, convert to rupees = amount × exchange rate.
↓
4. (Rectangle) Add 2% conversion fee to the converted cost.
↓
5. (Parallelogram) Display the expense category and cost in rupees; store the result.
↓
6. (Diamond/Loop) Are more expenses left? YES → Return to Step 3. NO → Continue.
↓
7. (Rectangle) Add all converted costs to calculate total spending.
↓
8. (Diamond) Is total spending ≤ budget?
   ├── YES → (Parallelogram) Display “Within budget”.
   └── NO → (Parallelogram) Display “Over budget”.
↓
9. (Rectangle) Find the category with the largest expense.
↓
10. (Parallelogram) Display total spending and largest expense category.
↓
11. (Oval) END
Python Source Code
expenses = [
    ("Hotel", 200, 83),
    ("Food", 100, 90),
    ("Transport", 50, 83)
]
budget = 30000
converted = []

for category, amount, rate in expenses:
    cost = amount * rate
    cost += cost * 0.02
    converted.append((category, cost))
    print(category, "Cost in INR: Rs.", round(cost, 2))

total = sum(item[1] for item in converted)
largest = max(converted, key=lambda item: item[1])
print("Total spending: Rs.", round(total, 2))
print("Budget:", "Within budget" if total <= budget else "Over budget")
print("Largest expense:", largest[0])
Sample Output
Hotel Cost in INR: Rs. 16932.0
Food Cost in INR: Rs. 9180.0
Transport Cost in INR: Rs. 4233.0
Total spending: Rs. 30345.0
Budget: Over budget
Largest expense: Hotel
Conclusion
The program converts expenses using the provided rates, adds fees, compares total spending against the budget and identifies the largest expense.
 
10. Campus Event Financial Planning
Problem Statement
Calculate event expenses, participant contributions, sponsorship shortfall and the minimum registrations needed to break even.
Objectives
Determine total event cost, funding gap and minimum number of paid registrations.
Assumptions
Venue ₹10000, equipment ₹5000, catering ₹200 per participant, transport ₹3000 and certificates ₹50 per participant. Sponsorship is ₹8000 and registration contribution is ₹400 per participant. Assume participant-dependent costs are incurred for each registration.
Algorithm
57.	Start.
58.	Read fixed costs, per-participant costs, sponsorship and contribution per participant.
59.	Calculate fixed and variable costs for the expected participants.
60.	Calculate total cost and funding gap after sponsorship.
61.	Calculate net contribution per participant after per-participant costs.
62.	Calculate the minimum registrations needed to cover fixed costs after sponsorship.
63.	Display the results and stop.
Flowchart (text form)
1. (Oval) START
↓
2. (Rectangle/Input) Read or set venue, equipment, transport, per-person catering, certificate cost, sponsorship, registration fee and expected participants.
↓
3. (Rectangle) Fixed cost = venue + equipment + transport.
↓
4. (Rectangle) Variable cost per participant = catering cost + certificate cost.
↓
5. (Rectangle) Total event cost = fixed cost + variable cost per participant × expected participants.
↓
6. (Rectangle) Participant funds = registration fee × expected participants.
↓
7. (Rectangle) Funding shortfall = maximum of 0 and (total cost − sponsorship − participant funds).
↓
8. (Rectangle) Net contribution per registration = registration fee − variable cost per participant.
↓
9. (Diamond) Is net contribution per registration > 0?
   ├── YES → (Rectangle) Minimum registrations = maximum of 0 and ceiling of (fixed cost − sponsorship) ÷ net contribution.
   └── NO → (Rectangle) Set minimum registrations to 0 (break-even cannot be reached using positive net contributions).
↓
10. (Parallelogram) Display fixed cost, total event cost, participant contributions, shortfall and minimum registrations.
↓
11. (Oval) END
Python Source Code
venue = 10000
equipment = 5000
transport = 3000
catering_per_person = 200
certificate_per_person = 50
sponsorship = 8000
registration_fee = 400
expected_participants = 100

fixed_cost = venue + equipment + transport
variable_per_person = catering_per_person + certificate_per_person
total_cost = fixed_cost + variable_per_person * expected_participants
participant_funds = registration_fee * expected_participants
shortfall = max(0, total_cost - sponsorship - participant_funds)

net_per_registration = registration_fee - variable_per_person
needed = 0
if net_per_registration > 0:
    needed = max(0, (fixed_cost - sponsorship + net_per_registration - 1)
                 // net_per_registration)

print("Fixed cost: Rs.", fixed_cost)
print("Total event cost: Rs.", total_cost)
print("Participant contributions: Rs.", participant_funds)
print("Funding shortfall: Rs.", shortfall)
print("Minimum registrations to break even:", needed)
Sample Output
Fixed cost: Rs. 18000
Total event cost: Rs. 43000
Participant contributions: Rs. 40000
Funding shortfall: Rs. 0
Minimum registrations to break even: 29
Conclusion
The program estimates event costs and funding, then calculates the minimum registration count required to cover fixed costs after sponsorship.
 
