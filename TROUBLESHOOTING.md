# 🔧 Troubleshooting Guide

> "Every error message is an opportunity to learn and improve. You've got this!"

*Last updated: January 2025*

This guide helps you quickly resolve common issues when working with Luminous Dynamics projects. If you don't find your answer here, check [SUPPORT.md](SUPPORT.md) for how to get help.

---

## 🚀 Quick Problem Finder

**Jump to your issue:**
- [Setup & Installation](#-setup--installation-issues)
- [Build Errors](#-build-errors)
- [Test Failures](#-test-failures)
- [Git & GitHub](#-git--github-issues)
- [Deployment & Runtime](#-deployment--runtime-issues)
- [Development Environment](#-development-environment-issues)

---

## 🏗️ Setup & Installation Issues

### Problem: "Command not found: npm" / "Command not found: cargo" / "Command not found: nix"

**Symptoms:**
```bash
$ npm install
bash: npm: command not found
```

**Cause:** Required tools not installed or not in PATH

**Solution:**

1. **Check if installed:**
   ```bash
   # For Node.js projects
   which npm node
   # Should show paths like /usr/bin/npm

   # For Rust projects
   which cargo rustc

   # For Nix projects
   which nix
   ```

2. **Install missing tools:**

   **Node.js (npm):**
   ```bash
   # macOS
   brew install node

   # Ubuntu/Debian
   sudo apt install nodejs npm

   # Or use nvm (recommended)
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   nvm install 18
   ```

   **Rust (cargo):**
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   source $HOME/.cargo/env
   ```

   **Nix:**
   ```bash
   # Multi-user (recommended)
   sh <(curl -L https://nixos.org/nix/install) --daemon
   ```

3. **Verify installation:**
   ```bash
   npm --version    # Should show version like 8.19.0
   cargo --version  # Should show version like 1.70.0
   nix --version    # Should show version like 2.18.0
   ```

---

### Problem: "Permission denied" during installation

**Symptoms:**
```bash
$ npm install -g some-package
Error: EACCES: permission denied
```

**Cause:** Trying to install global packages without proper permissions

**Solution:**

**Option 1: Use nvm** (recommended - no sudo needed)
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc  # or ~/.zshrc

# Install Node.js
nvm install 18
nvm use 18

# Now npm install -g works without sudo
npm install -g yarn
```

**Option 2: Fix npm permissions**
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

**Option 3: Use sudo** (not recommended)
```bash
sudo npm install -g package-name
```

---

### Problem: "Dependencies not resolving" / "Version conflicts"

**Symptoms:**
```bash
$ npm install
npm ERR! Could not resolve dependency
npm ERR! peer react@"^18.0.0" from some-package@1.0.0
```

**Cause:** Incompatible dependency versions

**Solution:**

1. **Clear cache and retry:**
   ```bash
   # For npm
   rm -rf node_modules package-lock.json
   npm cache clean --force
   npm install

   # For Cargo
   cargo clean
   rm Cargo.lock
   cargo build

   # For Poetry (Python)
   poetry cache clear --all pypi
   rm poetry.lock
   poetry install
   ```

2. **Check for version conflicts:**
   ```bash
   # npm
   npm ls <package-name>

   # Cargo
   cargo tree | grep <package-name>
   ```

3. **Update dependencies:**
   ```bash
   # npm
   npm update

   # Cargo
   cargo update
   ```

---

## 🔨 Build Errors

### Problem: "Module not found" / "Cannot find module"

**Symptoms:**
```bash
Error: Cannot find module './some-file'
Error: Module not found: Can't resolve 'some-package'
```

**Cause:** Missing dependency or incorrect import path

**Solution:**

1. **Install missing package:**
   ```bash
   # If it's a package
   npm install some-package

   # Check if it's in package.json
   cat package.json | grep some-package
   ```

2. **Check import path:**
   ```javascript
   // ❌ Wrong
   import { foo } from './utils/helper'  // Missing .js extension in ES modules

   // ✅ Correct
   import { foo } from './utils/helper.js'

   // ❌ Wrong
   import { bar } from '../../../utils'  // Fragile relative path

   // ✅ Better
   import { bar } from '@/utils'  // Use path alias
   ```

3. **Verify file exists:**
   ```bash
   ls -la src/utils/helper.js
   ```

---

### Problem: TypeScript compilation errors

**Symptoms:**
```bash
error TS2304: Cannot find name 'React'
error TS2345: Argument of type 'string' is not assignable to parameter of type 'number'
```

**Cause:** Type mismatches or missing type declarations

**Solution:**

1. **Install type declarations:**
   ```bash
   # For React
   npm install --save-dev @types/react @types/react-dom

   # For Node.js
   npm install --save-dev @types/node

   # Search for types
   npm search @types/<package-name>
   ```

2. **Fix type errors:**
   ```typescript
   // ❌ Type error
   const count: number = "5";

   // ✅ Fixed - convert type
   const count: number = parseInt("5", 10);

   // ❌ Type error
   function greet(name: string) {
     return `Hello, ${name}`;
   }
   greet(123);  // Error!

   // ✅ Fixed - pass correct type
   greet("Alice");
   ```

3. **Temporarily bypass** (not recommended for production):
   ```typescript
   // Use any sparingly
   const data: any = someFunctionReturningUnknownType();

   // Or use type assertion
   const result = (data as SomeType).property;
   ```

---

### Problem: Rust compilation errors

**Symptoms:**
```bash
error[E0425]: cannot find value `foo` in this scope
error[E0308]: mismatched types
```

**Cause:** Rust's strict type system catching issues

**Solution:**

1. **Read the error message carefully** (Rust errors are excellent!)
   ```bash
   # Rust tells you exactly what's wrong and how to fix it
   error[E0425]: cannot find value `count` in this scope
    --> src/main.rs:5:13
     |
   5 |     println!("{}", count);
     |                    ^^^^^ not found in this scope
     |
   help: consider importing this struct
     |
   1 | use std::sync::atomic::AtomicUsize;
   ```

2. **Common fixes:**
   ```rust
   // ❌ Unused variable
   let x = 5;  // warning: unused variable

   // ✅ Fix - prefix with underscore if intentionally unused
   let _x = 5;

   // ❌ Moved value
   let s = String::from("hello");
   takes_ownership(s);
   println!("{}", s);  // Error: value moved!

   // ✅ Fix - clone or use reference
   let s = String::from("hello");
   takes_ownership(s.clone());
   println!("{}", s);  // Works!
   ```

3. **Update Rust:**
   ```bash
   rustup update stable
   ```

---

## 🧪 Test Failures

### Problem: Tests passing locally but failing in CI

**Symptoms:**
- ✅ `npm test` locally succeeds
- ❌ GitHub Actions CI fails with same tests

**Cause:** Environment differences (timing, file paths, env vars)

**Solution:**

1. **Check for timing issues:**
   ```javascript
   // ❌ Flaky test - real timing
   test('async operation', () => {
     startAsync();
     setTimeout(() => {
       expect(result).toBe(true);
     }, 100);  // Might be too short in CI
   });

   // ✅ Reliable test
   test('async operation', async () => {
     await startAsync();
     expect(result).toBe(true);
   });
   ```

2. **Check environment variables:**
   ```bash
   # Local .env might have values CI doesn't
   # Check CI configuration (GitHub Actions .yml)

   # Use .env.example as template
   cp .env.example .env.test
   ```

3. **Run tests in CI-like environment:**
   ```bash
   # Use Docker to simulate CI
   docker run --rm -v $(pwd):/app node:18 npm test

   # Or use act to run GitHub Actions locally
   act -j test
   ```

---

### Problem: "Test suite failed to run"

**Symptoms:**
```bash
Test suite failed to run
SyntaxError: Cannot use import statement outside a module
```

**Cause:** Jest/test runner configuration issue

**Solution:**

1. **For ES modules (import/export):**
   ```json
   // package.json
   {
     "type": "module",
     "jest": {
       "transform": {
         "^.+\\.jsx?$": "babel-jest"
       }
     }
   }
   ```

2. **Install Babel:**
   ```bash
   npm install --save-dev @babel/preset-env
   ```

3. **Create babel.config.js:**
   ```javascript
   module.exports = {
     presets: [
       ['@babel/preset-env', { targets: { node: 'current' } }]
     ]
   };
   ```

---

## 📦 Git & GitHub Issues

### Problem: "Permission denied (publickey)"

**Symptoms:**
```bash
$ git push
Permission denied (publickey).
fatal: Could not read from remote repository.
```

**Cause:** SSH key not set up or not added to GitHub

**Solution:**

1. **Check if SSH key exists:**
   ```bash
   ls -la ~/.ssh/id_*.pub
   ```

2. **Generate new SSH key if needed:**
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   # Press Enter to accept defaults
   ```

3. **Add to SSH agent:**
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

4. **Add to GitHub:**
   ```bash
   # Copy public key
   cat ~/.ssh/id_ed25519.pub

   # Go to GitHub → Settings → SSH and GPG keys → New SSH key
   # Paste the key
   ```

5. **Test connection:**
   ```bash
   ssh -T git@github.com
   # Should say: "Hi username! You've successfully authenticated"
   ```

**Alternative: Use HTTPS instead:**
```bash
git remote set-url origin https://github.com/username/repo.git
```

---

### Problem: "Merge conflicts"

**Symptoms:**
```bash
$ git pull
Auto-merging file.txt
CONFLICT (content): Merge conflict in file.txt
```

**Cause:** Same lines changed in both branches

**Solution:**

1. **Find conflicted files:**
   ```bash
   git status
   # Shows: "both modified: file.txt"
   ```

2. **Open file and resolve:**
   ```
   <<<<<<< HEAD
   Your changes
   =======
   Their changes
   >>>>>>> branch-name

   # Edit to keep what you want:
   Final combined version
   ```

3. **Mark as resolved:**
   ```bash
   git add file.txt
   git commit -m "Resolve merge conflict in file.txt"
   ```

**Prevention tip:**
```bash
# Keep your branch up to date
git checkout main
git pull
git checkout your-branch
git merge main  # Or git rebase main
```

---

## 🚀 Deployment & Runtime Issues

### Problem: "Port already in use"

**Symptoms:**
```bash
Error: listen EADDRINUSE: address already in use :::3000
```

**Cause:** Another process using the port

**Solution:**

1. **Find process using port:**
   ```bash
   # macOS/Linux
   lsof -i :3000

   # Or use netstat
   netstat -vanp tcp | grep 3000
   ```

2. **Kill the process:**
   ```bash
   kill -9 <PID>

   # Or kill all node processes (careful!)
   killall node
   ```

3. **Use different port:**
   ```bash
   # Temporarily
   PORT=3001 npm start

   # Or in .env
   echo "PORT=3001" >> .env
   ```

---

### Problem: "Environment variable not found"

**Symptoms:**
```bash
Error: Missing environment variable: DATABASE_URL
TypeError: Cannot read property 'API_KEY' of undefined
```

**Cause:** .env file missing or not loaded

**Solution:**

1. **Create .env file:**
   ```bash
   # Copy example
   cp .env.example .env

   # Edit with your values
   nano .env
   ```

2. **Ensure .env is loaded:**
   ```javascript
   // At top of entry file (e.g., index.js)
   require('dotenv').config();

   // Or for ES modules
   import 'dotenv/config';
   ```

3. **Verify variables:**
   ```javascript
   console.log('DATABASE_URL:', process.env.DATABASE_URL);
   ```

**Note:** .env files are gitignored for security. Never commit secrets!

---

## 🖥️ Development Environment Issues

### Problem: "Hot reload not working"

**Symptoms:**
- Save file, but browser doesn't update
- Webpack/Vite not detecting changes

**Cause:** File watcher issues or configuration

**Solution:**

1. **Increase file watch limit (Linux):**
   ```bash
   echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
   sudo sysctl -p
   ```

2. **Check configuration:**
   ```javascript
   // vite.config.js
   export default {
     server: {
       watch: {
         usePolling: true  // For Docker/VMs
       }
     }
   }
   ```

3. **Restart dev server:**
   ```bash
   # Kill and restart
   pkill -f "node.*vite"
   npm run dev
   ```

---

### Problem: Out of memory during build

**Symptoms:**
```bash
FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed
JavaScript heap out of memory
```

**Cause:** Large build, insufficient Node.js memory

**Solution:**

1. **Increase Node memory:**
   ```bash
   # Temporary (4GB)
   NODE_OPTIONS="--max-old-space-size=4096" npm run build

   # Or add to package.json
   {
     "scripts": {
       "build": "NODE_OPTIONS='--max-old-space-size=4096' next build"
     }
   }
   ```

2. **Optimize build:**
   ```javascript
   // webpack.config.js
   module.exports = {
     optimization: {
       splitChunks: {
         chunks: 'all'
       }
     }
   };
   ```

---

## 🆘 Still Stuck?

If you don't find your issue here:

1. **Search existing issues:** [github.com/Luminous-Dynamics/.github/issues](https://github.com/Luminous-Dynamics/.github/issues)
2. **Ask in Discussions:** [github.com/orgs/Luminous-Dynamics/discussions](https://github.com/orgs/Luminous-Dynamics/discussions)
3. **Check project-specific docs:** Each repo has its own README and docs
4. **Contact support:** See [SUPPORT.md](SUPPORT.md)

**When asking for help, include:**
- Operating system (macOS/Linux/Windows + version)
- Tool versions (`node --version`, `npm --version`, etc.)
- Full error message (not screenshot)
- Steps to reproduce
- What you've tried already

---

## 📚 Related Resources

- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Initial setup and onboarding
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[PLAYBOOKS.md](PLAYBOOKS.md)** - Step-by-step guides for common tasks
- **[SUPPORT.md](SUPPORT.md)** - Getting help and support

---

*This troubleshooting guide is maintained with care and consciousness by the Luminous Dynamics community. Found a solution not listed here? Please contribute by opening a PR!*
