"""Offline regression tests of proposed privacy and threat gates (no inference)."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def audit_contract(policy, threat, manifest, api):
    missing = []
    for field in ("data_classification", "network_egress"):
        if field not in manifest and field not in policy:
            missing.append("missing disclosure: " + field)
    for marker in ("PROPOSED / NOT_IMPLEMENTED", "DENY / NOT_CONFIGURED",
                   "NOT_RUN", "retencj", "log", "endpoint"):
        if marker not in policy:
            missing.append("privacy marker: " + marker)
    for marker in ("PROPOSED / NOT_IMPLEMENTED", "prompt injection",
                   "audio", "wideo", "network_egress", "DENY / NOT_CONFIGURED"):
        if marker not in threat:
            missing.append("threat marker: " + marker)
    if api.get("public_entrypoints") != []:
        missing.append("unexpected public runtime API in scaffold")
    return missing


class PrivacyDesignTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.privacy = (ROOT / "docs/privacy.md").read_text(encoding="utf-8")
        cls.threat = (ROOT / "docs/security/threat-model.md").read_text(encoding="utf-8")
        cls.manifest = json.loads((ROOT / "config/component.json").read_text(encoding="utf-8"))
        cls.api = json.loads((ROOT / "contracts/api.json").read_text(encoding="utf-8"))

    def test_scaffold_privacy_and_threat_contract(self):
        self.assertEqual([], audit_contract(self.privacy, self.threat, self.manifest, self.api))

    def test_missing_egress_disclosure_is_regression(self):
        modified = self.privacy.replace("network_egress", "outbound_control")
        errors = audit_contract(modified, self.threat, self.manifest, self.api)
        self.assertIn("missing disclosure: network_egress", errors)

    def test_missing_data_classification_is_regression(self):
        modified = self.privacy.replace("data_classification", "classification_future")
        errors = audit_contract(modified, self.threat, self.manifest, self.api)
        self.assertIn("missing disclosure: data_classification", errors)

    def test_missing_deny_by_default_is_regression(self):
        modified = self.privacy.replace("DENY / NOT_CONFIGURED", "ALLOW")
        errors = audit_contract(modified, self.threat, self.manifest, self.api)
        self.assertIn("privacy marker: DENY / NOT_CONFIGURED", errors)

    def test_missing_multimodal_threat_assessment_is_regression(self):
        modified = self.threat.replace("prompt injection", "generic input")
        errors = audit_contract(self.privacy, modified, self.manifest, self.api)
        self.assertIn("threat marker: prompt injection", errors)


if __name__ == "__main__":
    unittest.main()
