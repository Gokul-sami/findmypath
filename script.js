import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js';
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'https://www.gstatic.com/firebasejs/9.0.0/firebase-auth.js';

const firebaseConfig = {
  apiKey: "AIzaSyAPAt8yoHglBADaGEhWGM1kZVgOzWhw8rE",
  authDomain: "findyourpath-bcf56.firebaseapp.com",
  projectId: "findyourpath-bcf56",
  storageBucket: "findyourpath-bcf56.appspot.com",
  messagingSenderId: "205317328979",
  appId: "1:205317328979:web:d49c38e66dc9821a4276a6",
  measurementId: "G-2YW6EBNFN2"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Handle form submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  signInWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
      console.log('Signed in:', userCredential.user);
      window.location.href = 'home.html';
    })
    .catch((error) => {
      if (error.code === 'auth/user-not-found') {
        createUserWithEmailAndPassword(auth, email, password)
          .then((userCredential) => {
            console.log('User registered and signed in:', userCredential.user);
            window.location.href = 'home.html';
          })
          .catch((createError) => {
            console.error('Error creating user:', createError.message);
            alert('Error creating user: ' + createError.message);
          });
      } else {
        console.error('Error signing in:', error.message);
        alert('Error: ' + error.message);
      }
    });
});
