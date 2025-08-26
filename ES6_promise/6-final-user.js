import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName) {
  const content = Promise.allSettled([uploadPhoto(fileName), signUpUser(firstName, lastName)]);

  return content
  .then((result) => {
    [
      {
        status: result.status,
        value: result.status === 'fulfilled' ? result.value : String(result.reason)
      }
    ]
  });
}
