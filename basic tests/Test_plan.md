# Test Plan – MeroChulo (Recipe Web Application)

## 1. Objective
To verify that the MeroChulo web application functions correctly, allowing users to register, log in, add recipes, and view recipes securely and efficiently.

---

## 2. Scope

### In Scope
- User Registration
- User Login/Logout
- Recipe Creation
- Recipe Viewing
- Input Validation
- Authentication & Authorization
- UI elements (including live clock)

### Out of Scope
- Third-party integrations
- Advanced scalability testing

---

## 3. Test Items
- Authentication Module
- Recipe Module
- UI Components
- Backend APIs (Django)
- Database (SQLite)

---

## 4. Test Types
- Functional Testing
- UI Testing
- Negative Testing
- Security Testing
- Usability Testing

---

## 5. Test Environment

| Component | Details |
|----------|--------|
| OS | Windows |
| Browser | Chrome, Firefox |
| Backend | Django |
| Database | SQLite |

---

## 6. Entry Criteria
- Application accessible
- Requirements finalized
- Test cases prepared

---

## 7. Exit Criteria
- All critical test cases passed
- No high-severity bugs open
- Application is stable

---

## 8. Test Scenarios
1. User registration with valid/invalid inputs
2. User login with correct/incorrect credentials
3. Logout functionality
4. Add recipe (valid/invalid data)
5. View recipes
6. Access control for unauthenticated users
7. Input validation checks
8. Error message display
9. Unauthorized access prevention
10. Live clock display

---

## 9. Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Authentication failure | High | Proper validation & testing |
| Data loss | Medium | Backup & DB validation |
| UI issues | Low | Cross-browser testing |

---

## 10. Deliverables
- Test Plan
- Test Scenarios
- Test Cases
- Bug Reports
- Test Summary Report