/** Raster export: exact art, optimized PNG. SVG type is outlined, so no font fetch. */
import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const modules = process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES;
const sharp = require(modules ? path.join(modules,'sharp') : 'sharp');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const dir = path.join(root,'assets/makeover');
const args = process.argv.slice(2);
if (args.length && args.length !== 2) throw new Error('Usage: render.mjs [source.svg destination.png]');
if (args.length === 2) {
  await sharp(args[0]).png({compressionLevel:9,palette:true,colours:128,effort:10,dither:0}).toFile(args[1]);
} else {
const jobs=[['avatar-static.svg','avatar.png'],['profile-banner-static.svg','profile-banner.png'],['social-preview-static.svg','social-preview.png']];
for (const file of await fs.readdir(path.join(dir,'social'))) if(file.endsWith('.svg'))jobs.push([`social/${file}`,`social/${file.replace('.svg','.png')}`]);
for(const [src,dest] of jobs) await sharp(path.join(dir,src)).png({compressionLevel:9,palette:true,colours:128,effort:10,dither:0}).toFile(path.join(dir,dest));
console.log(`Rendered ${jobs.length} PNG assets.`);

}
