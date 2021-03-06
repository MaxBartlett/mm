#include "z_bg_iknin_susceil.h"

#define FLAGS 0x00000030

#define THIS ((BgIkninSusceil*)thisx)

void BgIkninSusceil_Init(Actor* thisx, GlobalContext* globalCtx);
void BgIkninSusceil_Destroy(Actor* thisx, GlobalContext* globalCtx);
void BgIkninSusceil_Update(Actor* thisx, GlobalContext* globalCtx);
void BgIkninSusceil_Draw(Actor* thisx, GlobalContext* globalCtx);

/*
const ActorInit Bg_Iknin_Susceil_InitVars = {
    ACTOR_BG_IKNIN_SUSCEIL,
    ACTORCAT_BG,
    FLAGS,
    OBJECT_IKNINSIDE_OBJ,
    sizeof(BgIkninSusceil),
    (ActorFunc)BgIkninSusceil_Init,
    (ActorFunc)BgIkninSusceil_Destroy,
    (ActorFunc)BgIkninSusceil_Update,
    (ActorFunc)BgIkninSusceil_Draw,
};
*/

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0A740.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0A804.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0A838.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0A86C.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0A95C.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/BgIkninSusceil_Init.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/BgIkninSusceil_Destroy.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AB14.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AB44.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AB88.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0ABA8.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AC74.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AC90.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0ACD4.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0ACE8.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AD44.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AD64.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AE3C.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/func_80C0AE5C.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/BgIkninSusceil_Update.asm")

#pragma GLOBAL_ASM("./asm/non_matchings/overlays/ovl_Bg_Iknin_Susceil_0x80C0A740/BgIkninSusceil_Draw.asm")
