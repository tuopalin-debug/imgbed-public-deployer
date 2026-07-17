import unittest
from pathlib import Path


WORKFLOW_PATH = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "deploy.yml"
WORKFLOW = WORKFLOW_PATH.read_text(encoding="utf-8")


class WorkersDevSubdomainWorkflowTests(unittest.TestCase):
    def test_worker_subdomain_is_initialized_before_resource_inspection(self):
        export_account = WORKFLOW.index("- name: Export Cloudflare account env")
        ensure_subdomain = WORKFLOW.index("- name: Ensure workers.dev subdomain")
        inspect_state = WORKFLOW.index("- name: Inspect Cloudflare state")
        ensure_kv = WORKFLOW.index("- name: Ensure KV namespace")

        self.assertLess(export_account, ensure_subdomain)
        self.assertLess(ensure_subdomain, inspect_state)
        self.assertLess(ensure_subdomain, ensure_kv)

    def test_worker_subdomain_uses_existing_oauth_permission_and_official_api(self):
        self.assertIn("if: ${{ env.DEPLOY_TYPE == 'worker' }}", WORKFLOW)
        self.assertIn('workers/subdomain', WORKFLOW)
        self.assertIn('ERROR_CODE" != "10007"', WORKFLOW)
        self.assertIn('sha256sum', WORKFLOW)
        self.assertIn('linya-$SUBDOMAIN_HASH', WORKFLOW)
        self.assertIn('-X PUT', WORKFLOW)


if __name__ == "__main__":
    unittest.main()
