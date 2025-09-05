import express from 'express';
import router from './routes/index.js';

const app = express();
const port = process.env.PORT || 1245;

app.use('/', router);

app.listen(port, () => {
  console.log(`Server app listening on port ${port}`);
});

export default app;
