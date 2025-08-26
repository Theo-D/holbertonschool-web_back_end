import { uploadPhoto } from "./utils";
import { createUser } from "./utils";

export default async function handleProfileSignup() {
  try {
    const content = await Promise.all([uploadPhoto(), createUser()]);
    console.log(`${content[0].body} ${content[1].firstName} ${content[1].lastName}`);
  } catch {
    return console.log('Signup system offline');
  }
}
