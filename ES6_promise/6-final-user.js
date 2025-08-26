import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const content = Promise.allSettled([uploadPhoto(fileName), signUpUser(firstName, lastName)]);

  const result = await content;
  result.map((res) => ({
    status: res.status,
    value: res.status === 'fulfilled' ? res.value : String(res.reason),
  }));

  return result;
}
