#!/usr/bin/env python3
"""
Final Comprehensive NPM Supply Chain Attack Security Audit Script
================================================================

This script analyzes package.json and package-lock.json files to detect
compromised packages from both NPM supply chain attacks in September 2025.

Author: Security Audit Team
Date: 2025
"""

import json
import os
import sys
from typing import Dict, List, Set, Tuple
import re

class FinalNPMSecurityAuditor:
    def __init__(self):
        # Complete list of compromised packages from both attacks
        self.compromised_packages = {
            # Attack 1: September 8, 2025 - Crypto Wallet Hijacking Attack
            "backslash": {
                "affected_versions": ["0.2.1"],
                "attack_date": "2025-09-08",
                "description": "Backslash package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "0.26M"
            },
            "chalk-template": {
                "affected_versions": ["1.1.1"],
                "attack_date": "2025-09-08",
                "description": "Chalk template package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "3.9M"
            },
            "supports-hyperlinks": {
                "affected_versions": ["4.1.1"],
                "attack_date": "2025-09-08",
                "description": "Supports hyperlinks package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "19.2M"
            },
            "has-ansi": {
                "affected_versions": ["6.0.1"],
                "attack_date": "2025-09-08",
                "description": "Has ansi package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "12.1M"
            },
            "simple-swizzle": {
                "affected_versions": ["0.2.3"],
                "attack_date": "2025-09-08",
                "description": "Simple swizzle package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "26.26M"
            },
            "color-string": {
                "affected_versions": ["2.1.1"],
                "attack_date": "2025-09-08",
                "description": "Color string package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "27.48M"
            },
            "error-ex": {
                "affected_versions": ["1.3.3"],
                "attack_date": "2025-09-08",
                "description": "Error ex package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "47.17M"
            },
            "color-name": {
                "affected_versions": ["2.0.1"],
                "attack_date": "2025-09-08",
                "description": "Color name package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "191.71M"
            },
            "is-arrayish": {
                "affected_versions": ["0.3.3"],
                "attack_date": "2025-09-08",
                "description": "Is arrayish package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "73.8M"
            },
            "slice-ansi": {
                "affected_versions": ["7.1.1"],
                "attack_date": "2025-09-08",
                "description": "Slice ansi package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "59.8M"
            },
            "color-convert": {
                "affected_versions": ["3.1.1"],
                "attack_date": "2025-09-08",
                "description": "Color convert package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "193.5M"
            },
            "wrap-ansi": {
                "affected_versions": ["9.0.1"],
                "attack_date": "2025-09-08",
                "description": "Wrap ansi package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "197.99M"
            },
            "ansi-regex": {
                "affected_versions": ["6.2.1"],
                "attack_date": "2025-09-08",
                "description": "Ansi regex package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "243.64M"
            },
            "supports-color": {
                "affected_versions": ["10.2.1"],
                "attack_date": "2025-09-08",
                "description": "Supports color package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "287.1M"
            },
            "strip-ansi": {
                "affected_versions": ["7.1.1"],
                "attack_date": "2025-09-08",
                "description": "Strip ansi package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "261.17M"
            },
            "chalk": {
                "affected_versions": ["5.6.1"],
                "attack_date": "2025-09-08",
                "description": "Chalk package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "299.99M"
            },
            "debug": {
                "affected_versions": ["4.4.2"],
                "attack_date": "2025-09-08",
                "description": "Debug package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "357.6M"
            },
            "ansi-styles": {
                "affected_versions": ["6.2.2"],
                "attack_date": "2025-09-08",
                "description": "Ansi styles package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "371.41M"
            },
            "proto-tinker-wc": {
                "affected_versions": ["0.1.87"],
                "attack_date": "2025-09-08",
                "description": "Proto tinker wc package compromised with crypto wallet hijacking malware",
                "severity": "CRITICAL",
                "weekly_downloads": "Unknown"
            },
            
            # Attack 2: September 16, 2025 - Advanced Malware with Auto-Trojanization
            "@ctrl/tinycolor": {
                "affected_versions": ["4.1.1", "4.1.2"],
                "attack_date": "2025-09-16",
                "description": "Tinycolor package compromised with advanced malware (2.2M weekly downloads)",
                "severity": "CRITICAL",
                "weekly_downloads": "2.2M"
            },
            "angulartics2": {
                "affected_versions": ["14.1.2"],
                "attack_date": "2025-09-16",
                "description": "Angulartics2 package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/deluge": {
                "affected_versions": ["7.2.2"],
                "attack_date": "2025-09-16",
                "description": "Deluge package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/golang-template": {
                "affected_versions": ["1.4.3"],
                "attack_date": "2025-09-16",
                "description": "Golang template package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/magnet-link": {
                "affected_versions": ["4.0.4"],
                "attack_date": "2025-09-16",
                "description": "Magnet link package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/ngx-codemirror": {
                "affected_versions": ["7.0.2"],
                "attack_date": "2025-09-16",
                "description": "NGX Codemirror package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/ngx-csv": {
                "affected_versions": ["6.0.2"],
                "attack_date": "2025-09-16",
                "description": "NGX CSV package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/ngx-emoji-mart": {
                "affected_versions": ["9.2.2"],
                "attack_date": "2025-09-16",
                "description": "NGX Emoji Mart package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/ngx-rightclick": {
                "affected_versions": ["4.0.2"],
                "attack_date": "2025-09-16",
                "description": "NGX Rightclick package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/qbittorrent": {
                "affected_versions": ["9.7.2"],
                "attack_date": "2025-09-16",
                "description": "QBittorrent package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/react-adsense": {
                "affected_versions": ["2.0.2"],
                "attack_date": "2025-09-16",
                "description": "React AdSense package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/shared-torrent": {
                "affected_versions": ["6.3.2"],
                "attack_date": "2025-09-16",
                "description": "Shared Torrent package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/torrent-file": {
                "affected_versions": ["4.1.2"],
                "attack_date": "2025-09-16",
                "description": "Torrent File package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/transmission": {
                "affected_versions": ["7.3.1"],
                "attack_date": "2025-09-16",
                "description": "Transmission package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@ctrl/ts-base32": {
                "affected_versions": ["4.0.2"],
                "attack_date": "2025-09-16",
                "description": "TS Base32 package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "encounter-playground": {
                "affected_versions": ["0.0.5"],
                "attack_date": "2025-09-16",
                "description": "Encounter Playground package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "json-rules-engine-simplified": {
                "affected_versions": ["0.2.4", "0.2.1"],
                "attack_date": "2025-09-16",
                "description": "JSON Rules Engine Simplified package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "koa2-swagger-ui": {
                "affected_versions": ["5.11.2", "5.11.1"],
                "attack_date": "2025-09-16",
                "description": "Koa2 Swagger UI package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/gesturehandler": {
                "affected_versions": ["2.0.35"],
                "attack_date": "2025-09-16",
                "description": "NativeScript Gesture Handler package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/sentry": {
                "affected_versions": ["4.6.43"],
                "attack_date": "2025-09-16",
                "description": "NativeScript Sentry package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/text": {
                "affected_versions": ["1.6.13"],
                "attack_date": "2025-09-16",
                "description": "NativeScript Text package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/ui-collectionview": {
                "affected_versions": ["6.0.6"],
                "attack_date": "2025-09-16",
                "description": "NativeScript UI Collection View package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/ui-drawer": {
                "affected_versions": ["0.1.30"],
                "attack_date": "2025-09-16",
                "description": "NativeScript UI Drawer package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/ui-image": {
                "affected_versions": ["4.5.6"],
                "attack_date": "2025-09-16",
                "description": "NativeScript UI Image package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/ui-material-bottomsheet": {
                "affected_versions": ["7.2.72"],
                "attack_date": "2025-09-16",
                "description": "NativeScript UI Material Bottom Sheet package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/ui-material-core": {
                "affected_versions": ["7.2.76"],
                "attack_date": "2025-09-16",
                "description": "NativeScript UI Material Core package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "@nativescript-community/ui-material-core-tabs": {
                "affected_versions": ["7.2.76"],
                "attack_date": "2025-09-16",
                "description": "NativeScript UI Material Core Tabs package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "ngx-color": {
                "affected_versions": ["10.0.2"],
                "attack_date": "2025-09-16",
                "description": "NGX Color package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "ngx-toastr": {
                "affected_versions": ["19.0.2"],
                "attack_date": "2025-09-16",
                "description": "NGX Toastr package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "ngx-trend": {
                "affected_versions": ["8.0.1"],
                "attack_date": "2025-09-16",
                "description": "NGX Trend package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "react-complaint-image": {
                "affected_versions": ["0.0.35"],
                "attack_date": "2025-09-16",
                "description": "React Complaint Image package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "react-jsonschema-form-conditionals": {
                "affected_versions": ["0.3.21"],
                "attack_date": "2025-09-16",
                "description": "React JSON Schema Form Conditionals package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "react-jsonschema-form-extras": {
                "affected_versions": ["1.0.4"],
                "attack_date": "2025-09-16",
                "description": "React JSON Schema Form Extras package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "rxnt-authentication": {
                "affected_versions": ["0.0.6"],
                "attack_date": "2025-09-16",
                "description": "RXNT Authentication package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "rxnt-healthchecks-nestjs": {
                "affected_versions": ["1.0.5"],
                "attack_date": "2025-09-16",
                "description": "RXNT Healthchecks NestJS package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "rxnt-kue": {
                "affected_versions": ["1.0.7"],
                "attack_date": "2025-09-16",
                "description": "RXNT Kue package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "swc-plugin-component-annotate": {
                "affected_versions": ["1.9.2"],
                "attack_date": "2025-09-16",
                "description": "SWC Plugin Component Annotate package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            "ts-gaussian": {
                "affected_versions": ["3.0.6"],
                "attack_date": "2025-09-16",
                "description": "TS Gaussian package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            },
            # Additional packages that may be affected
            "tinycolor": {
                "affected_versions": ["*"],
                "attack_date": "2025-09-16",
                "description": "Tinycolor package compromised with advanced malware",
                "severity": "HIGH",
                "weekly_downloads": "Unknown"
            }
        }
        
        self.vulnerabilities_found = []
        self.project_paths = []

    def load_json_file(self, file_path: str) -> Dict:
        """Load and parse a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: File not found: {file_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file {file_path}: {e}")
            return {}

    def check_version_vulnerability(self, package_name: str, version: str) -> bool:
        """Check if a specific package version is vulnerable."""
        if package_name not in self.compromised_packages:
            return False
            
        affected_versions = self.compromised_packages[package_name]["affected_versions"]
        
        # If all versions are affected
        if "*" in affected_versions:
            return True
            
        # Check specific versions
        return version in affected_versions

    def analyze_package_json(self, package_json_path: str) -> List[Dict]:
        """Analyze package.json for direct dependencies."""
        vulnerabilities = []
        package_data = self.load_json_file(package_json_path)
        
        if not package_data:
            return vulnerabilities
            
        # Check dependencies
        for dep_type in ['dependencies', 'devDependencies', 'peerDependencies']:
            if dep_type in package_data:
                for package_name, version_spec in package_data[dep_type].items():
                    if self.check_version_vulnerability(package_name, version_spec):
                        vulnerabilities.append({
                            'package': package_name,
                            'version': version_spec,
                            'type': dep_type,
                            'file': package_json_path,
                            'severity': self.compromised_packages[package_name]['severity'],
                            'attack_info': self.compromised_packages[package_name]
                        })
        
        return vulnerabilities

    def analyze_package_lock(self, package_lock_path: str) -> List[Dict]:
        """Analyze package-lock.json for all dependencies including transitive ones."""
        vulnerabilities = []
        lock_data = self.load_json_file(package_lock_path)
        
        if not lock_data or 'packages' not in lock_data:
            return vulnerabilities
            
        # Check all packages in the lock file
        for package_path, package_info in lock_data['packages'].items():
            if 'version' in package_info:
                # Extract package name from path
                package_name = package_path.replace('node_modules/', '').split('/')[-1]
                
                # Handle scoped packages
                if package_path.startswith('node_modules/@'):
                    parts = package_path.replace('node_modules/', '').split('/')
                    if len(parts) >= 2:
                        package_name = f"{parts[0]}/{parts[1]}"
                
                version = package_info['version']
                
                if self.check_version_vulnerability(package_name, version):
                    vulnerabilities.append({
                        'package': package_name,
                        'version': version,
                        'type': 'transitive' if 'node_modules' in package_path else 'direct',
                        'file': package_lock_path,
                        'path': package_path,
                        'severity': self.compromised_packages[package_name]['severity'],
                        'attack_info': self.compromised_packages[package_name]
                    })
        
        return vulnerabilities

    def scan_project(self, project_path: str) -> Dict:
        """Scan a project for vulnerabilities."""
        results = {
            'project_path': project_path,
            'package_json_vulns': [],
            'package_lock_vulns': [],
            'total_vulnerabilities': 0,
            'critical_vulnerabilities': 0,
            'high_vulnerabilities': 0,
            'attack_1_vulnerabilities': 0,
            'attack_2_vulnerabilities': 0
        }
        
        # Check for package.json
        package_json_path = os.path.join(project_path, 'package.json')
        if os.path.exists(package_json_path):
            results['package_json_vulns'] = self.analyze_package_json(package_json_path)
        
        # Check for package-lock.json
        package_lock_path = os.path.join(project_path, 'package-lock.json')
        if os.path.exists(package_lock_path):
            results['package_lock_vulns'] = self.analyze_package_lock(package_lock_path)
        
        all_vulns = results['package_json_vulns'] + results['package_lock_vulns']
        results['total_vulnerabilities'] = len(all_vulns)
        
        # Count by severity and attack
        for vuln in all_vulns:
            if vuln['severity'] == 'CRITICAL':
                results['critical_vulnerabilities'] += 1
            elif vuln['severity'] == 'HIGH':
                results['high_vulnerabilities'] += 1
            
            if vuln['attack_info']['attack_date'] == '2025-09-08':
                results['attack_1_vulnerabilities'] += 1
            elif vuln['attack_info']['attack_date'] == '2025-09-16':
                results['attack_2_vulnerabilities'] += 1
        
        return results

    def generate_report(self, results: List[Dict]) -> str:
        """Generate a comprehensive security report."""
        report = []
        report.append("=" * 120)
        report.append("FINAL COMPREHENSIVE NPM SUPPLY CHAIN ATTACK SECURITY AUDIT REPORT")
        report.append("=" * 120)
        report.append("")
        
        total_vulnerabilities = sum(r['total_vulnerabilities'] for r in results)
        total_critical = sum(r['critical_vulnerabilities'] for r in results)
        total_high = sum(r['high_vulnerabilities'] for r in results)
        total_attack_1 = sum(r['attack_1_vulnerabilities'] for r in results)
        total_attack_2 = sum(r['attack_2_vulnerabilities'] for r in results)
        
        report.append(f"EXECUTIVE SUMMARY:")
        report.append(f"- Total projects scanned: {len(results)}")
        report.append(f"- Total vulnerabilities found: {total_vulnerabilities}")
        report.append(f"- Critical vulnerabilities: {total_critical}")
        report.append(f"- High vulnerabilities: {total_high}")
        report.append(f"- Attack 1 (Crypto Wallet Hijacking): {total_attack_1}")
        report.append(f"- Attack 2 (Advanced Malware): {total_attack_2}")
        report.append("")
        
        if total_vulnerabilities == 0:
            report.append("[SAFE] NO VULNERABILITIES DETECTED")
            report.append("Your projects appear to be safe from both NPM supply chain attacks.")
        else:
            if total_critical > 0:
                report.append("[CRITICAL] CRITICAL VULNERABILITIES DETECTED")
            else:
                report.append("[WARNING] HIGH SEVERITY VULNERABILITIES DETECTED")
            report.append("The following vulnerabilities were found in your projects:")
        
        report.append("")
        report.append("=" * 120)
        
        for result in results:
            if result['total_vulnerabilities'] > 0:
                report.append(f"\nPROJECT: {result['project_path']}")
                report.append("-" * 60)
                report.append(f"Total Vulnerabilities: {result['total_vulnerabilities']}")
                report.append(f"Critical: {result['critical_vulnerabilities']}, High: {result['high_vulnerabilities']}")
                report.append(f"Attack 1: {result['attack_1_vulnerabilities']}, Attack 2: {result['attack_2_vulnerabilities']}")
                report.append("")
                
                all_vulns = result['package_json_vulns'] + result['package_lock_vulns']
                for vuln in all_vulns:
                    report.append(f"Package: {vuln['package']}")
                    report.append(f"Version: {vuln['version']}")
                    report.append(f"Type: {vuln['type']}")
                    report.append(f"Severity: {vuln['severity']}")
                    report.append(f"Attack Date: {vuln['attack_info']['attack_date']}")
                    report.append(f"Weekly Downloads: {vuln['attack_info'].get('weekly_downloads', 'Unknown')}")
                    report.append(f"Description: {vuln['attack_info']['description']}")
                    if 'path' in vuln:
                        report.append(f"Path: {vuln['path']}")
                    report.append("")
        
        # Add malware indicators
        report.append("=" * 120)
        report.append("MALWARE INDICATORS OF COMPROMISE:")
        report.append("=" * 120)
        report.append("")
        report.append("ATTACK 1 - Crypto Wallet Hijacking:")
        report.append("- Phishing Domain: npmjs.help")
        report.append("- Target: Cryptocurrency transactions and wallet interactions")
        report.append("- Method: Browser-based malware that intercepts crypto activity")
        report.append("- Affected: 18 packages with 2+ billion weekly downloads")
        report.append("")
        report.append("ATTACK 2 - Advanced Malware:")
        report.append("- bundle.js SHA-256: 46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09")
        report.append("- Exfiltration endpoint: hxxps://webhook[.]site/bb8ca5f6-4175-45d2-b042-fc9ebb8170b7")
        report.append("- Malicious GitHub Actions workflows in .github/workflows/")
        report.append("- Unauthorized npm publishes or package modifications")
        report.append("")
        
        # Add recommendations
        report.append("=" * 120)
        report.append("IMMEDIATE ACTIONS REQUIRED:")
        report.append("=" * 120)
        
        if total_vulnerabilities > 0:
            report.append("1. CRITICAL ACTIONS:")
            report.append("   - IMMEDIATELY uninstall or pin to known-good versions")
            report.append("   - Audit environments (CI/CD agents, developer laptops) for unauthorized activity")
            report.append("   - Rotate npm tokens and other exposed secrets")
            report.append("   - Monitor logs for unusual npm publish or package modification events")
            report.append("   - Check for malicious GitHub Actions workflows")
            report.append("   - Scan for bundle.js files with the specified SHA-256")
            report.append("   - Clean npm cache and reinstall all packages")
            report.append("   - Use package lock files with pinned versions")
            report.append("")
        
        report.append("2. PREVENTIVE MEASURES:")
        report.append("   - Enable 2FA on all developer accounts")
        report.append("   - Implement automated dependency scanning in CI/CD")
        report.append("   - Regular security audits of dependencies")
        report.append("   - Use tools like 'npm audit', Snyk, or OWASP Dependency Check")
        report.append("   - Keep dependencies updated to latest secure versions")
        report.append("   - Implement package signing verification")
        report.append("   - Consider using Aikido SafeChain for secure package management")
        report.append("")
        
        report.append("3. MONITORING:")
        report.append("   - Set up alerts for new security vulnerabilities")
        report.append("   - Monitor package update frequencies and sources")
        report.append("   - Regular security training for development team")
        report.append("   - Monitor for suspicious network activity to known IOCs")
        report.append("   - Implement Software Bill of Materials (SBOM) tracking")
        report.append("")
        
        return "\n".join(report)

    def run_audit(self, project_paths: List[str]) -> str:
        """Run the complete security audit."""
        print("Starting Final Comprehensive NPM Supply Chain Attack Security Audit...")
        print(f"Scanning {len(project_paths)} project(s)...")
        print(f"Checking against {len(self.compromised_packages)} known compromised packages...")
        print("Including both Attack 1 (crypto wallet hijacking) and Attack 2 (advanced malware) attacks")
        
        results = []
        for project_path in project_paths:
            print(f"Scanning: {project_path}")
            result = self.scan_project(project_path)
            results.append(result)
            print(f"  - Total vulnerabilities: {result['total_vulnerabilities']}")
            print(f"  - Critical: {result['critical_vulnerabilities']}, High: {result['high_vulnerabilities']}")
            print(f"  - Attack 1: {result['attack_1_vulnerabilities']}, Attack 2: {result['attack_2_vulnerabilities']}")
        
        report = self.generate_report(results)
        return report

def main():
    """Main function to run the final comprehensive security audit."""
    auditor = FinalNPMSecurityAuditor()
    
    # Default project paths (modify as needed)
    default_paths = [
        r"C:\Users\zayds\Documents\Orion",
        r"C:\Users\zayds\Documents\Orion\functions"
    ]
    
    # Allow command line arguments for custom paths
    if len(sys.argv) > 1:
        project_paths = sys.argv[1:]
    else:
        project_paths = default_paths
    
    # Filter to only existing paths
    existing_paths = [path for path in project_paths if os.path.exists(path)]
    
    if not existing_paths:
        print("Error: No valid project paths found.")
        print("Usage: python security-audit-final.py [project_path1] [project_path2] ...")
        sys.exit(1)
    
    # Run the audit
    report = auditor.run_audit(existing_paths)
    
    # Print report to console
    print("\n" + report)
    
    # Save report to file
    report_file = "final-comprehensive-security-audit-report.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\nFinal comprehensive report saved to: {report_file}")

if __name__ == "__main__":
    main()
