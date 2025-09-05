import readDatabase from '../utils.js';

export default class StudentsController {
  static async getAllStudents(request, response) {
    const dbPath = process.argv[2];
    let studentsByField = '';

    try {
      studentsByField = await readDatabase(dbPath);
    } catch (err) {
      response.status(500);
      throw new Error('Cannot load the database');
    }

    let responseObj = 'This is the list of our students';

    for (const [key, value] of Object.entries(studentsByField)) {
      const studentsString = value.join(', ');
      responseObj += `\nNumber of students in ${key}: ${value.length}. List: ${studentsString}`;
    }

    response.status(200).send(responseObj);
  }

  static async getAllStudentsByMajor(request, response) {
    let studentsByField = '';
    const majorVal = request.params.major;
    const dbPath = process.argv[2];

    if (majorVal !== 'SWE' && majorVal !== 'CS') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      studentsByField = await readDatabase(dbPath);
    } catch (err) {
      response.status(500);
      throw new Error('Cannot load the database');
    }

    const responseObj = `List: ${studentsByField[majorVal].join(', ')}`;
    console.log(responseObj);

    response.status(200).send(responseObj);
  }
}
