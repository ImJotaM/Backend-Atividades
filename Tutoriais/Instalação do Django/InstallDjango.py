import os
import shutil
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

def print_header():
    
    print(Fore.GREEN + r"""
    ____    _                       
   / __ \  (_)___ _____  ____ _____ 
  / / / / / / __ `/ __ \/ __ `/ __ \
 / /_/ / / / /_/ / / / / /_/ / /_/ /
/_____/_/ /\__,_/_/ /_/\__, /\____/ 
     /___/            /____/                                
""")
    print(Fore.GREEN + "=========== Framework Web ===========")
    print()

def is_django_installed():
    try:
        subprocess.run(["python", "-m", "django", "--version"], capture_output=True, check=True)
        return True
    except:
        return False
        
def get_django_version():
    try:
        result = subprocess.run(["python", "-m", "django", "--version"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except:
        return None

def install_django():
    try:
        result = subprocess.run(["pip", "install", "django"], capture_output=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"\n❌ Falha crítica: {e}")
        return None
        
def is_python_installed():
    try:
        subprocess.run(["python", "--version"], capture_output=True, check=True)
        return True
    except:
        return False

def get_python_version():
    try:
        result = subprocess.run(["python", "--version"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except:
        return None

def install_python():
    try:
        result = subprocess.run(["scoop", "install", "python"], capture_output=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"\n❌ Falha crítica: {e}")
        return None
        
def is_scoop_installed():
    return shutil.which("scoop") is not None

def install_scoop():
    install_command = """
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    """
    try:
        result = subprocess.run(["powershell","-Command", install_command], check=True)
        return result
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"\n❌ Falha crítica: {e}")
        return None
    
class DjangoInstaller:
    
    @staticmethod
    def check_and_install_items():
        
        print(Fore.BLUE + "🔍 Verificando se o Django está instalado...")
        
        if not is_django_installed():
            
            print(Fore.YELLOW + "\n⚠️  Django não encontrado no sistema.")
            print("📦 Preparando instalação do Django...")
            
            print(Fore.BLUE + "\n🔍 Verificando se o Python está instalado...")
            
            if not is_python_installed():
                
                print(Fore.YELLOW + "\n⚠️  Python não encontrado no sistema.\n")
                print("📦 Preparando instalação do Python...")
                
                print("\n🔍 Verificando se o Scoop está instalado...")
                
                if not is_scoop_installed():
                    
                    print(Fore.YELLOW + "\n⚠️  Scoop não encontrado no sistema.")
                    print(Fore.MAGENTA + "🔧  Baixando e instalando o Scoop...")
                    print(Style.DIM + "Isso pode levar alguns minutos...")    
                    
                    result_scoop = install_scoop()
                    if result_scoop and result_scoop.returncode == 0:
                        print(Fore.GREEN + Style.BRIGHT + f"\n✅ Scoop instalado com sucesso!")
                    else:
                        print(Fore.RED + "\n❌ Erro durante a instalação do Scoop:")
                        if result_scoop:
                            print(Style.DIM + result_python.stderr)
                        return
                    
                else:
                    print("✅ Scoop já está instalado.")
                
                print(Fore.MAGENTA + "\n🔧  Baixando e instalando o Python...")
                print(Style.DIM + "Isso pode levar alguns minutos...")
            
                result_python = install_python()
                if result_python and result_python.returncode == 0:
                    print(Fore.GREEN + Style.BRIGHT + f"\n✅ Python {get_python_version()} instalado com sucesso!")
                else:
                    print(Fore.RED + "\n❌ Erro durante a instalação do Python:")
                    if result_python:
                        print(Style.DIM + result_python.stderr)
                    return
            
            else:
                print(Fore.GREEN + f"✅ Python já instalado (Versão: {get_python_version()})!")
                
            print(Fore.MAGENTA + "\n🔧  Baixando e instalando o Django...")
            print(Style.DIM + "Isso pode levar alguns minutos...")
            
            result_django = install_django()
            if result_django and result_django.returncode == 0:
                
                print(Fore.GREEN + Style.BRIGHT + f"\n🎉 Django {get_django_version()} instalado com sucesso!")
                
                print(Fore.CYAN +  "Próximos passos sugeridos:")
                print("1. Crie um novo projeto: 'django-admin startproject <meuprojeto>'")
                print("2. Execute o servidor: 'python manage.py runserver'")

            else:
                print(Fore.RED + "\n❌ Erro durante a instalação do Django:")
                if result_django:
                    print(Style.DIM + result_django.stderr)
                return
                
        else:
            print(Fore.GREEN + f"\n✅ Django já está instalado (Versão: {get_django_version()})")
            print(Style.DIM +   "Dica: Use 'python -m pip install --upgrade django' para atualizar.")
            
def main():
    
    print_header()
    
    DjangoInstaller.check_and_install_items()
    
    print()
    os.system("pause")

if __name__ == "__main__":
    main()