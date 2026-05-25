import { Command } from "@oclif/core";
import { execSync } from "node:child_process";

const REPO_URL = "git@github.com:gaorun/my-labs.git";

export default class Install extends Command {
  static description = "Install all Agent Skills from the my-labs repository";

  async run(): Promise<void> {
    this.log("🚀 Installing all Agent Skills from my-labs...\n");

    try {
      execSync(`npx skills add ${REPO_URL}`, {
        stdio: "inherit",
      });
      this.log("\n✅ All skills installed successfully!");
    } catch (error) {
      this.error(error as Error);
    }
  }
}
