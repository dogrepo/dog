import Replicate from 'replicate'
import dotenv from 'dotenv'
import { writeFile } from 'fs/promises'
dotenv.config()

const replicate = new Replicate({
  auth: process.env.REPLICATE_API_TOKEN,
  userAgent: 'https://www.npmjs.com/package/create-replicate'
})
const model = 'stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc'
const input = {
  size: "1024x1024",
  style: "digital_illustration/hand_drawn",
  prompt: "A hand-drawn illustration of a shiba-inu dog."
};

const output = await replicate.run("recraft-ai/recraft-v3", { input });
await writeFile("ghdog.webp", output);
console.log(`Output saved to ghdog.webp`);
