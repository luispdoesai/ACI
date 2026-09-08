"""
Lead Enrichment Helper Script
Enriches raw lead records with domain heuristics, company size estimation, and email provider categorization.
"""

import sys
import json
from typing import Dict, Any


def enrich_lead(email: str, company_name: str = "") -> Dict[str, Any]:
    """Analyze domain and classify lead provider type."""
    if "@" not in email:
        return {"error": "Invalid email"}

    local_part, domain = email.strip().lower().split("@", 1)

    free_providers = {
        "gmail.com", "yahoo.com", "hotmail.com", "outlook.com",
        "icloud.com", "aol.com", "mail.com", "zoho.com", "proton.me", "protonmail.com"
    }

    is_custom_domain = domain not in free_providers
    estimated_company = company_name if company_name else (domain.split(".")[0].capitalize() if is_custom_domain else "Individual")

    return {
        "email": email,
        "domain": domain,
        "is_business_domain": is_custom_domain,
        "provider_type": "B2B Custom Domain" if is_custom_domain else "B2C / Personal Mail",
        "inferred_company": estimated_company,
        "suggested_tier": "Enterprise / B2B" if is_custom_domain else "Standard / B2C"
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lead_enricher.py <email> [company_name]")
        sys.exit(1)

    test_email = sys.argv[1]
    company = sys.argv[2] if len(sys.argv) > 2 else ""
    enrichment = enrich_lead(test_email, company)
    print(json.dumps(enrichment, indent=2))
