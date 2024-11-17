import dns.name
import dns.resolver

n = dns.name.from_text('example.com')
answer = dns.resolver.query(n,'A')
for rdata in answer:
    print(rdata.to_text())
