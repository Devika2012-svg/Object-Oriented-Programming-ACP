class Account:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin

    def show_pin_status(self):
        print("🔒 PIN is secure!")

    def check_pin(self, pin):
        if self.__pin == pin:
            print("✅ Correct PIN! Access granted.")
        else:
            print("❌ Incorrect PIN! Access denied.")

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("🎉 PIN updated successfully!")
        else:
            print("⚠️  Invalid PIN! Enter exactly 4 digits.")

    def __str__(self):
        return f"👤 Account Owner: {self.owner}\n🔒 PIN: ****"


my_account = Account("Devika", "1234")

print("🏦 WELCOME TO SMART BANKING 🏦")
print("-" * 32)

print(my_account)
my_account.show_pin_status()

print("\n🔎 Checking PINs:")
my_account.check_pin("1234")
my_account.check_pin("9999")

print("\n🛡️ Testing private PIN protection:")
my_account.__pin = "9999"

my_account.check_pin("9999")
my_account.check_pin("1234")

print("\n🔄 Updating PIN safely:")
my_account.set_pin("9999")
my_account.check_pin("9999")

print("\n🧪 Testing invalid PINs:")
my_account.set_pin("99")
my_account.set_pin("abcd")
my_account.set_pin("5678")

print("\n" + "=" * 32)
print("✨ THANKS FOR USING SMART BANKING! ✨")
print(my_account)
print("🔒Your account security is important!")
