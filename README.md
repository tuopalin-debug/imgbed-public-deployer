# ImgBed Public Deployer

这个公开仓库只负责运行免费的 GitHub Actions 部署流程。

正式图床部署代码保存在私有仓库 `tuopalin-debug/CloudFlare-ImgBed-pages` 中，本仓库的 workflow 每次运行时通过 `PRIVATE_DEPLOYER_TOKEN` 只读拉取私有代码，然后把私有代码目录部署到用户的 Cloudflare Pages 项目。

注意：不要把私有代码、访问令牌、Cloudflare OAuth token 写入本仓库文件或日志。
