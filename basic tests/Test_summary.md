# Test Summary Report – MeroChulo

## 1. Project Overview
MeroChulo is a Django-based recipe web application that allows users to register, log in, and manage recipes with a clean UI and secure authentication.

---

## 2. Testing Scope
- Functional testing of authentication and recipe features
- Validation testing
- UI/UX testing
- Security testing

---

## 3. Test Execution Summary

| Metric | Value |
|-------|------|
| Total Test Cases | 30 |
| Passed | 27 |
| Failed | 3 |
| Blocked | 0 |

---

## 4. Defect Summary

| Severity | Count |
|----------|------|
| Critical | 0 |
| High     | 1 |
| Medium   | 1 |
| Low      | 1 |
| Total    | 3 |

---

## 5. Key Issues Identified
- Improper validation for empty recipe fields
- Weak error messages on login failure
- Unauthorized users able to access restricted pages (edge case)

---

## 6. Test Coverage

| Module | Status |
|--------|-------|
| Registration | Covered |
| Login/Logout | Covered |
| Recipe Management | Covered |
| Validation | Covered |
| Security | Partially Covered |

---

## 7. Performance Summary
- Application response time is acceptable
- No major delays observed

---

## 8. Conclusion
The application is stable with minor issues. It is suitable for proper release after fixing high-priority defects.
