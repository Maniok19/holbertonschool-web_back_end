export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
      let grade = 'N/A';
      if (gradeObj) {
        grade = gradeObj.grade;
      }
      return {
        ...student,
        grade,
      };
    });
}
