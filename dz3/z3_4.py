class DotaHero:
    
    # атрибуты класса
    game: str = "Dota 2"
    max_level: int = 30

    def __init__(self, 
                 name: str, 
                 primary_attr: str, 
                 release_year: int, 
                 attack_type: str, 
                 health_growth: float, 
                 mana_growth: float, 
                 base_health: float, 
                 base_mana: float, 
                 level: int = 1) -> None:
        """
        Параметры:
            name: имя героя
            primary_attr: основной атрибут (сила, ловкость, интеллект)
            release_year: год добавления в игру
            attack_type: тип атаки (дальний или ближний)
            health_growth: прирост здоровья за уровень
            mana_growth: прирост маны за уровень
            base_health: здоровье на 1 уровне
            base_mana: мана на 1 уровне
        """

        self.name: str = name
        self.primary_attr: str = primary_attr
        self.release_year: int = release_year
        self.attack_type: str = attack_type
        self.health_growth: float = health_growth
        self.mana_growth: float = mana_growth
        self.base_health: float = base_health
        self.base_mana: float = base_mana
    def __str__(self) -> str: 
        return (f"{self.name} | {self.primary_attr} | {self.attack_type} | "
                f"HP: {self.base_health:.1f} | MP: {self.base_mana:.1f}")

    def health_at_level(self, level: int) -> float: # показывает количество здоровья на указанном уровне
        if level < 1:
            raise ValueError("Уровень не может быть меньше 1")
        if level > DotaHero.max_level:
            raise ValueError(f"Нельзя узнать здоровье на уровне выше {DotaHero.max_level}")
        return self.base_health + (level - 1) * self.health_growth

    def mana_at_level(self, level: int) -> float: # показывает количество маны на указанном уровне
        if level < 1:
            raise ValueError("Уровень не может быть меньше 1")
        if level > DotaHero.max_level:
            raise ValueError(f"Нельзя узнать ману на уровне выше {DotaHero.max_level}")
        return self.base_mana + (level - 1) * self.mana_growth

    def years_in_game(self, current_year: int) -> int: # сколько лет назад добавили героя
        return current_year - self.release_year

    def get_primary_attr(self) -> str: # возвращает основной атрибут героя
        return self.primary_attr
    
    def get_attack_type(self) -> str: # возвращает тип атаки героя
        return self.attack_type


# объекты
pudge = DotaHero(
    name="Pudge",
    primary_attr="сила",
    release_year=2013,
    attack_type="ближний",
    health_growth=80,
    mana_growth=20,
    base_health=700,
    base_mana=200
)

monkey_king = DotaHero(
    name="Monkey King",
    primary_attr="ловкость",
    release_year=2016,
    attack_type="ближний",
    health_growth=50,
    mana_growth=30,
    base_health=600,
    base_mana=250
)

muerta = DotaHero(
    name="Muerta",
    primary_attr="интеллект",
    release_year=2023,
    attack_type="дальний",
    health_growth=30,
    mana_growth=50,
    base_health=500,
    base_mana=300
)

print(pudge)
print(monkey_king)
print(muerta)

print(f"\nЗдоровье Pudge на 10 уровне: {pudge.health_at_level(10)}")
print(f"Мана Monkey King на 15 уровне: {monkey_king.mana_at_level(15)}")

# попытка узнать здоровье на 35 уровне (вызовет ошибку)
try:
    print(f"\nЗдоровье Pudge на 35 уровне: {pudge.health_at_level(35)}")
except ValueError as e:
    print(f"Ошибка: {e}")

print(f"\nMuerta в игре уже {muerta.years_in_game(2026)} лет")
print(f"Основной атрибут Muerta: {muerta.get_primary_attr()}")
print(f"Тип атаки Muerta: {muerta.get_attack_type()}")

print(f"\nАтрибуты класса: игра = {DotaHero.game}, макс. уровень = {DotaHero.max_level}")