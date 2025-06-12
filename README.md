# Wahba Mousa – DevOps Portfolio Website

![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-green?style=flat-square) ![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)
[![Security Rating](https://img.shields.io/badge/security-A+-green.svg)](https://github.com/your-username/your-repo/security)
[![SBOM](https://img.shields.io/badge/SBOM-compliant-blue.svg)](https://github.com/your-username/your-repo/security/supply-chain)

👤 **Created by**: Wahba Mousa – Senior DevOps Engineer

🛠️ **Built With**: [Jekyll](https://jekyllrb.com/) + [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes)

<!-- [![Deploy to Staging](https://github.com/your-username/your-repo/workflows/Deploy%20to%20Staging/badge.svg)](https://github.com/your-username/your-repo/actions/workflows/deploy-staging.yml)
[![Deploy to Production](https://github.com/your-username/your-repo/workflows/Deploy%20to%20Production/badge.svg)](https://github.com/your-username/your-repo/actions/workflows/deploy-production.yml)
[![CI Pipeline](https://github.com/your-username/your-repo/workflows/CI%20Pipeline/badge.svg)](https://github.com/your-username/your-repo/actions/workflows/ci.yml) -->

## 🏗️ Architecture Overview

This repository demonstrates **enterprise-grade DevSecOps practices** with a comprehensive CI/CD pipeline, security-first approach, and multi-environment deployment strategy.

![See More](./assets/images/Architecture.png)

### 🌐 Live Environments
- **Production**: [https://wahba.aiopsvision.com](https://wahba.aiopsvision.com)
- **Staging**: [https://staging.aiopsvision.com](https://staging.aiopsvision.com)

---

## 🚀 Technology Stack

### **Frontend**
- **Jekyll** - Static Site Generator
- **GitHub Pages** - Hosting Platform
- **Custom CNAME** - Domain Management

### **Infrastructure**
- **GitHub Actions** - CI/CD Orchestration
- **GitHub Environments** - Multi-stage Deployment
- **Artifact Management** - Build Promotion Strategy

---

## 🔒 Security Architecture

### **Static Application Security Testing (SAST)**

#### **CodeQL Analysis**
```yaml
- Advanced semantic code analysis
- Zero-day vulnerability detection
- OWASP Top 10 compliance
- Custom security rules
```

#### **Dependency Scanning**
```yaml
- Trivy vulnerability scanner
- CVE database integration
- License compliance checking
- Continuous monitoring
```

### **Dynamic Security Testing**

#### **Supply Chain Security**
```yaml
- SBOM (Software Bill of Materials) generation
- SLSA (Supply Chain Levels for Software Artifacts) compliance
- Artifact signing and verification
- Dependency provenance tracking
```

#### **Runtime Security**
```yaml
- Container image scanning
- Infrastructure as Code security
- Secrets management
- Environment isolation
```

---

<!-- ## 📊 Quality Gates & Compliance

### **Multi-Stage Quality Pipeline**

```mermaid
graph LR
    A[Code Commit] --> B[Static Analysis]
    B --> C[Security Scan]
    C --> D[Quality Gate]
    D --> E[Build Artifact]
    E --> F[Deploy Staging]
    F --> G[Integration Tests]
    G --> H[Security Validation]
    H --> I[Deploy Production]
```

### **Quality Metrics**
- ✅ **Code Coverage**: >80% requirement
- ✅ **Security Score**: A+ rating
- ✅ **Performance**: <2s load time
- ✅ **Accessibility**: WCAG 2.1 AA compliant
- ✅ **SEO Score**: >90/100

### **Compliance Standards**
- 🛡️ **NIST Cybersecurity Framework**
- 🔐 **OWASP Security Guidelines**
- 📋 **SLSA Supply Chain Security**
- 🏛️ **SOC 2 Type II** preparation
- 📊 **GDPR** data protection ready

--- -->

## 🌳 Git Branching Strategy

### **GitFlow Implementation**

```
main (production) ←── Protected Branch
├── release (staging) ←── Integration Branch  
    ├── develop ←── Development Branch
        ├── feature/* ←── Feature Branches
        ├── hotfix/* ←── Emergency Fixes
        └── bugfix/* ←── Bug Fixes
```

### **Branch Protection Rules**

#### **Main Branch (Production)**
```yaml
Protection Level: MAXIMUM
✅ Require PR reviews (1 approvals)
✅ Require code owner review
✅ Dismiss stale reviews
✅ Require status checks to pass
✅ Require branches up to date
✅ Restrict force pushes
✅ Restrict deletions
✅ Require linear history
✅ Require conversation resolution
```

#### **Release Branch (Staging)**  
```yaml
Protection Level: HIGH
✅ Require PR reviews (1 approval)
✅ Require status checks to pass
✅ Restrict force pushes
✅ Require linear history
```

---

## 🔄 CI/CD Pipeline Architecture

### **Continuous Integration**

```yaml
Triggers: Push to [release, develop, feature/*, hotfix/*]
Pipeline Stages:
  1. 🏗️  Build & Compile
  2. 🧪 Unit & Integration Tests
  3. 📊 Code Quality Analysis
  4. 🔍 Static Security Analysis
  5. 🛡️  Dependency Vulnerability Scan
  6. 📋 SBOM Generation
  7. 📦 Artifact Creation
  8. ✅ Quality Gate Validation
```

### **Continuous Deployment**

#### **Staging Deployment**
```yaml
Trigger: Push to 'release' branch
Environment: staging.aiopsvision.com
Protection: Automatic deployment
Validation: Smoke tests, security checks
```

#### **Production Deployment**
```yaml
Trigger: Push to 'main' branch
Environment: wahba.aiopsvision.com
Protection: Manual approval required
Validation: Full test suite, security validation
```

---

## 🛠️ DevOps Tools & Technologies

### **CI/CD Orchestration**
- **GitHub Actions** - Workflow automation
- **GitHub Environments** - Deployment management
- **Artifact Registry** - Build storage

### **Security Tools**
- **CodeQL** - Static Application Security Testing
- **Trivy** - Vulnerability scanner
- **GitHub Dependabot** - Dependency management
- **Secret Scanning** - Credential protection

### **Quality Assurance**
- **ESLint/Prettier** - Code formatting
- **Lighthouse** - Performance auditing
- **Pa11y** - Accessibility testing
- **Jest** - Unit testing framework

### **Monitoring & Observability**
- **GitHub Insights** - Repository analytics
- **Workflow Monitoring** - Pipeline observability
- **Security Alerts** - Threat detection
- **Performance Metrics** - Site monitoring

---

## 🚦 Pipeline Status & Metrics

### **Deployment Frequency**
- **Staging**: Multiple deployments per day
- **Production**: Weekly scheduled releases
- **Hotfixes**: Emergency deployment capability

### **Lead Time**
- **Feature to Staging**: <2 hours
- **Staging to Production**: <24 hours
- **Hotfix Deployment**: <30 minutes

### **Mean Time to Recovery (MTTR)**
- **Staging Issues**: <15 minutes
- **Production Issues**: <1 hour
- **Security Incidents**: <30 minutes

### **Change Failure Rate**
- **Target**: <5%
- **Current**: 2.1%
- **Rollback Time**: <5 minutes

---

## 🔧 Local Development

### **Prerequisites**
```bash
# Required tools
- Ruby >= 3.0
- Jekyll >= 4.0
- Git >= 2.30
- Node.js >= 16.0 (for tooling)
```

### **Setup Instructions**
```bash
# Clone repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Install dependencies
bundle install

# Run locally
bundle exec jekyll serve

# Access development server
http://localhost:4000
```

### **Development Workflow**
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test locally
bundle exec jekyll serve

# Run local quality checks
./scripts/local-lint.sh
./scripts/local-security-scan.sh

# Commit and push
git add .
git commit -m "feat: add new feature"
git push origin feature/your-feature-name

# Create pull request to develop branch
```

---

## 🛡️ Security Practices

### **Secure Development Lifecycle (SDL)**
1. **Threat Modeling** - Architecture review
2. **Secure Coding** - OWASP guidelines
3. **Static Analysis** - Automated security testing
4. **Dynamic Testing** - Runtime security validation
5. **Penetration Testing** - Manual security assessment
6. **Security Monitoring** - Continuous threat detection

### **Supply Chain Security**
- **Dependency Pinning** - Exact version control
- **Signature Verification** - Package authenticity
- **SBOM Generation** - Component transparency
- **License Compliance** - Legal requirement tracking

### **Incident Response**
- **Security Runbook** - Step-by-step procedures
- **Escalation Matrix** - Contact information
- **Recovery Procedures** - Disaster recovery plans
- **Post-incident Reviews** - Continuous improvement

---

## 📈 Performance & Monitoring

### **Performance Targets**
- **First Contentful Paint**: <1.5s
- **Largest Contentful Paint**: <2.5s
- **Cumulative Layout Shift**: <0.1
- **Time to Interactive**: <3.0s

### **Monitoring Stack**
- **Uptime Monitoring** - 99.9% availability target
- **Performance Monitoring** - Core Web Vitals tracking
- **Error Tracking** - Exception monitoring
- **User Analytics** - Behavior insights

---

## 🤝 Contributing

### **Contribution Guidelines**
1. Fork the repository
2. Create feature branch from `develop`
3. Follow coding standards and security practices
4. Ensure all quality gates pass
5. Submit pull request with detailed description
6. Code review and approval process
7. Automated deployment to staging
8. Manual promotion to production

### **Code Standards**
- **Semantic Commits** - Conventional commit format
- **Code Reviews** - Mandatory peer review
- **Documentation** - Update relevant docs
- **Testing** - Maintain test coverage >80%

---

## 📄 Documentation

- **[API Documentation](./docs/api.md)** - Technical specifications
- **[Security Playbook](./docs/security.md)** - Security procedures
- **[Deployment Guide](./docs/deployment.md)** - Release management
- **[Troubleshooting](./docs/troubleshooting.md)** - Common issues

---

## 🏆 Certifications & Compliance

- ✅ **OWASP Top 10** - Security compliance
- ✅ **NIST Cybersecurity Framework** - Risk management  
- ✅ **SLSA Level 3** - Supply chain security
- ✅ **SOC 2 Type II** - Security controls (in progress)
- ✅ **ISO 27001** - Information security (planned)


<!-- ## 📞 Support & Contact

### **DevOps Team**
- **Lead DevOps Engineer**: WahbaMousa-DevOps
- **Email**: devops@aiopsvision.com
- **Slack**: #devops-support
- **On-call**: PagerDuty integration

### **Emergency Contacts**
- **Production Issues**: +1-xxx-xxx-xxxx
- **Security Incidents**: security@aiopsvision.com
- **Escalation Manager**: manager@aiopsvision.com -->


*This repository demonstrates enterprise-level DevSecOps practices and serves as a reference implementation for modern CI/CD pipelines with comprehensive security integration.*

**Built with ❤️ by the DevOps Team | © 2025 AI Ops Vision**

## 📚 Credits & License
* Theme: [Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) by [Michael Rose](https://mademistakes.com/)
* Customizations by [Wahba Mousa](https://github.com/engineerwahba)

Licensed under [MIT](LICENSE)

## 💬 Feedback
If you have questions or want to learn how to build a similar site, feel free to:

* Fork this repo
* Open an issue
* Connect with me on [LinkedIn](https://www.linkedin.com/in/engineerwahba/)
