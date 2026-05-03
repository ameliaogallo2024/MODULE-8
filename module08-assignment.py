# Module 8 Assignment


# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Computing": 200,
    "Cybersecurity": 225,
    "IT Support": 100
}

# TODO 2: Create customer dictionaries
customer1 = {
    "company_name": "TechNova", 
    "contact_person": "Alice Ward", 
    "email": "alice@technova.com", 
    "phone": "555-0101"
}
customer2 = {
    "company_name": "GreenGrid", 
    "contact_person": "Bob Miller", 
    "email": "bob@greengrid.org", 
    "phone": "555-0202"
}
customer3 = {
    "company_name": "BlueSky Inc", 
    "contact_person": "Charlie Day", 
    "email": "charlie@bluesky.com", 
    "phone": "555-0303"
}
customer4 = {
    "company_name": "Solaris", 
    "contact_person": "Diana Prince", 
    "email": "diana@solaris.io", 
    "phone": "555-0404"
}

# TODO 3: Create a master customers dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for cid, info in customers.items():
    print(f"ID: {cid} | Company: {info['company_name']} | Contact: {info['contact_person']}")

# TODO 5: Look up specific customers
print("\n\nCustomer Lookups:")
print("-" * 60)
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print(f"C002 Info: {c002_info}")
print(f"C003 Contact: {c003_contact}")
print(f"C999 Lookup: {c999_info}")

# TODO 6: Update customer information
print("\n\nUpdating Customer Information:")
print("-" * 60)
customers["C001"]["phone"] = "555-9999"
customers["C002"]["industry"] = "Renewable Energy"
print(f"Updated C001 Phone: {customers['C001']['phone']}")
print(f"Updated C002 Industry: {customers['C002']['industry']}")

# TODO 7: Create project dictionaries for each customer
projects = {
    "C001": [
        {"name": "E-Commerce Site", "service": "Web Development", "hours": 40, "budget": 6000, "status": "completed"},
        {"name": "Data Dashboard", "service": "Data Analysis", "hours": 20, "budget": 3500, "status": "active"}
    ],
    "C002": [
        {"name": "Cloud Migration", "service": "Cloud Computing", "hours": 50, "budget": 10000, "status": "active"}
    ],
    "C003": [
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 30, "budget": 6750, "status": "pending"}
    ],
    "C004": [] # No projects for C004 yet
}

# TODO 8: Calculate project costs
print("\n\nProject Cost Calculations:")
print("-" * 60)
for cid, proj_list in projects.items():
    for proj in proj_list:
        rate = services[proj["service"]]
        cost = rate * proj["hours"]
        print(f"Project: {proj['name']} | Calculated Cost: ${cost}")

# TODO 9: Customer statistics using dictionary methods
print("\n\nCustomer Statistics:")
print("-" * 60)
all_ids = list(customers.keys())
all_companies = [c["company_name"] for c in customers.values()]
total_customers = len(customers)
print(f"IDs: {all_ids}")
print(f"Companies: {all_companies}")
print(f"Total Customers: {total_customers}")

# TODO 10: Service usage analysis
print("\n\nService Usage Analysis:")
print("-" * 60)
service_counts = {}
for proj_list in projects.values():
    for proj in proj_list:
        srv = proj["service"]
        service_counts[srv] = service_counts.get(srv, 0) + 1
print(f"Usage counts: {service_counts}")

# TODO 11: Financial aggregations
print("\n\nFinancial Summary:")
print("-" * 60)
all_project_flat = [p for sublist in projects.values() for p in sublist]
total_hours = sum(p["hours"] for p in all_project_flat)
total_budget = sum(p["budget"] for p in all_project_flat)
avg_budget = total_budget / len(all_project_flat) if all_project_flat else 0
max_budget = max(p["budget"] for p in all_project_flat)
min_budget = min(p["budget"] for p in all_project_flat)

print(f"Total Hours: {total_hours} | Total Budget: ${total_budget}")
print(f"Average Budget: ${avg_budget:.2f}")
print(f"Max/Min Budget: ${max_budget} / ${min_budget}")

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)
for cid, info in customers.items():
    cust_projs = projects.get(cid, [])
    p_count = len(cust_projs)
    p_hours = sum(p["hours"] for p in cust_projs)
    p_budget = sum(p["budget"] for p in cust_projs)
    print(f"{info['company_name']} ({cid}): Projects: {p_count}, Hours: {p_hours}, Budget: ${p_budget}")

# TODO 13: Rate adjustments using dictionary comprehension
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
active_customers = {cid: info for cid, info in customers.items() if len(projects.get(cid, [])) > 0}
print("\n\nActive Customers (with projects):")
print("-" * 60)
print(list(active_customers.keys()))

# TODO 15: Create project summaries using dictionary comprehension
customer_budgets = {cid: sum(p["budget"] for p in projs) for cid, projs in projects.items()}
print("\n\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
service_tiers = {s: ("Premium" if r >= 200 else "Standard" if r >= 100 else "Basic") for s, r in services.items()}
print("\n\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Customer validation function
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]
    return all(field in customer_dict for field in required)

print("\n\nCustomer Validation:")
print("-" * 60)
for cid, info in customers.items():
    print(f"Customer {cid} valid: {validate_customer(info)}")

# TODO 18: Project status tracking with loops and conditionals
status_counts = {}
for proj_list in projects.values():
    for p in proj_list:
        stat = p["status"]
        status_counts[stat] = status_counts.get(stat, 0) + 1

print("\n\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Budget analysis function with aggregation
def analyze_customer_budgets(projects_dict):
    stats = {}
    for cid, projs in projects_dict.items():
        if not projs:
            stats[cid] = {'total': 0, 'average': 0, 'count': 0}
            continue
        total = sum(p["budget"] for p in projs)
        stats[cid] = {
            'total': total,
            'average': total / len(projs),
            'count': len(projs)
        }
    return stats

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
print(analyze_customer_budgets(projects))

# TODO 20: Service recommendation system
def recommend_services(customer_id, customers, projects, services):
    used_services = {p["service"] for p in projects.get(customer_id, [])}
    recommendations = [s for s in services.keys() if s not in used_services]
    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)
print(f"Recommendations for C001: {recommend_services('C001', customers, projects, services)}")