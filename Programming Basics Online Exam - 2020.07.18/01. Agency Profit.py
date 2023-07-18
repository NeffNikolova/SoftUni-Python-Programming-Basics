company_name = input()
normal_tickets_nr = int(input())
children_tickets_nr = int(input())
normal_ticket_net_price = float(input())
service_price = float(input())

children_ticket_net_price = 0.3 * normal_ticket_net_price

agency_income = 0.2 * ((normal_tickets_nr * (normal_ticket_net_price + service_price)) + ((children_tickets_nr * (children_ticket_net_price + service_price))))

print (f'The profit of your agency from {company_name} tickets is {agency_income:.2f} lv.')