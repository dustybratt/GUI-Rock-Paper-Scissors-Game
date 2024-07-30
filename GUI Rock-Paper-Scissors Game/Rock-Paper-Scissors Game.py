# Import Required Library
from tkinter import *
from tkinter import ttk
from random import *

# Create Object
root = Tk()

# Set geometry
root.geometry("500x500")

root.title("Rock-Paper-Scissors-Game")

# List of players
list = ["rock","paper","scissors"]

choose_number = randint(0,2)
print(choose_number) # For testing if it works

label = Label(root,text="Computer ",width = 20,height=4,font=("algerian",15))
label.pack()

def spin():
    choose_number = randint(0,2)
    label.config(text=list[choose_number])
    if user_select.get() == "Rock":
        user_select_value = 0
        print(user_select_value)
    elif user_select.get() == "Paper":
        user_select_value = 1
        print(user_select_value)
    elif user_select.get() == "Scissors":
        user_select_value = 2
        print(user_select_value)

    if user_select_value == 0:
        if choose_number == 0:
            wl_label.config(text="Tie! - "+" Computer:Bad luck")
        elif choose_number == 1:
            wl_label.config(text="YOU Loose - "+" Computer: I am better ")
        elif choose_number == 2 :
            wl_label.config(text="YOU Won - "+" Computer: You won by luck")

    elif user_select_value == 1:
        if choose_number == 1:
            wl_label.config(text="Tie! - "+" Computer: Nice game")
        elif choose_number == 0:
            wl_label.config(text="YOU Won - "+" Computer: Shit how you are better")
        elif choose_number == 2 :
            wl_label.config(text="YOU Loose - "+" Computer: booo")

    elif user_select_value == 2:
        if choose_number == 2:
            wl_label.config(text="Tie!")
        elif choose_number == 0:
            wl_label.config(text="YOU Loose - "+" Computer: I am playing this game since i was born")
        elif choose_number == 1 :
            wl_label.config(text="YOU Won")



# Adding dropdown box for Rock,Paper,Scissors
user_select = ttk.Combobox(root,value=["Rock","Paper","Scissors"])
user_select.current(0)
user_select.pack()

# Add Labels,Button
wl_label = Label(root,text="",font=("arial",17),width=50,height=4)
wl_label.pack()

button = Button(root,text="Spin!",font=("bell mt",10),command=spin)
button.pack()

root.mainloop()
..
.
.
.
.
.
/
.
.
main
...
////

....

/////
.....
/////
....
//
main
*****
  </div>
        <button class="btn">Add transaction</button>
      </form>
    </div>
    <!-- Notification -->
    <div class="notification-container" id="notification">
      <p>Please add a description and amount</p>
    </div>
    <script src="script.js"></script>
  </body>
</html>
  </div>
        <button class="btn">Add transaction</button>
      </form>
    </div>
    <!-- Notification -->
    <div class="notification-container" id="notification">
      <p>Please add a description and amount</p>
    </div>
    <script src="script.js"></script>
  </body>
</html>
  </div>
        <button class="btn">Add transaction</button>
      </form>
    </div>
    <!-- Notification -->
    <div class="notification-container" id="notification">
      <p>Please add a description and amount</p>
    </div>
    <script src="script.js"></script>
  </body>
</html>
  </div>
        <button class="btn">Add transaction</button>
      </form>
    </div>
    <!-- Notification -->
    <div class="notification-container" id="notification">
      <p>Please add a description and amount</p>
    </div>
    <script src="script.js"></script>
  </body>
</html>
@media screen and (min-width: 740px) {
  .card {
    width: 35rem;
    padding: 0rem 5rem;
  }

  .sneaker img {
    width: 20rem;
  }

  .circle {
    width: 15rem;
    height: 15rem;
  }

  .info h1 {
    font-size: 3rem;
  }

  .info h3 {
    font-size: 1.3rem;
  }
}.

/////////////////////////
///////////////////////////
/////////////////////////////////
////////////////
//////////////////////
////////////////////////
////////////////////////
////////////////////////////////
////////////////////////////
///////////////////////////////
//////////////////////////////
///////////////////////////////
//////////////////////////////
/////////////////////////
////////////////
////////////////////
////////////////////////
/////////////////////////
////////////////////
//////////////////////
//////////////////////////
//////////////////////
//////////////////////////
/////////////////////////
///////////////////////
////////////////////////
///////////////////
/////////
/////////////////////////
//////////////////
////////////////
////////////
////////////
///////////////
/////////
///////////
////////////
///////////
.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}.card-info {
  margin: 20px;
  font-family: var(--secondary-font);
  text-align: center;
  line-height: 20px;
}

.btn-container {
  text-align: center;
  margin-top: 10px;
}

/* SECTION 4 */
.testimonial {
  height: 100vh;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background: #000;
  color: #fff;
}
  //Popback
  title.style.transform = "translateZ(0px)";
  sneaker.style.transform = "translateZ(0) rotateZ(0deg)";
  description.style.transform = "translateZ(0px)";
  sizes.style.transform = "translateZ(0px)";
  purchase.style.transform = "translateZ(0px)";
});
.  //Popback
  title.style.transform = "translateZ(0px)";
  sneaker.style.transform = "translateZ(0) rotateZ(0deg)";
  description.style.transform = "translateZ(0px)";
  sizes.style.transform = "translateZ(0px)";
  purchase.style.transform = "translateZ(0px)";
});
.  //Popback
  title.style.transform = "translateZ(0px)";
  sneaker.style.transform = "translateZ(0) rotateZ(0deg)";
  description.style.transform = "translateZ(0px)";
  sizes.style.transform = "translateZ(0px)";
  purchase.style.transform = "translateZ(0px)";
});
.  //Popback
  title.style.transform = "translateZ(0px)";
  sneaker.style.transform = "translateZ(0) rotateZ(0deg)";
  description.style.transform = "translateZ(0px)";
  sizes.style.transform = "translateZ(0px)";
  purchase.style.transform = "translateZ(0px)";
});
.  //Popback
  title.style.transform = "translateZ(0px)";
  sneaker.style.transform = "translateZ(0) rotateZ(0deg)";
  description.style.transform = "translateZ(0px)";
  sizes.style.transform = "translateZ(0px)";
  purchase.style.transform = "translateZ(0px)";
});
.  //Popback
  title.style.transform = "translateZ(0px)";
  sneaker.style.transform = "translateZ(0) rotateZ(0deg)";
  description.style.transform = "translateZ(0px)";
  sizes.style.transform = "translateZ(0px)";
  purchase.style.transform = "translateZ(0px)";
});
.
