import torch


class Optimizer:

    @staticmethod
    def SGD_CosineAnnealingLR(model, T_max, SGD_lr, SGD_m=0.9, weight_decay=0, eta_min=0):
        """
        :param model: torch model
        :param T_max: CosineAnnealingLR Maximum number of iterations (0~π steps).
        :param SGD_lr: SGD lr
        :param SGD_m: SGD momentum
        :param eta_min: CosineAnnealingLR Minimum learning rate.
        :param weight_decay: SGD weight decay.
        :return: optimizer and scheduler
        """
        optimizer = torch.optim.SGD(model.parameters(), lr=SGD_lr, momentum=SGD_m, weight_decay=weight_decay)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max, eta_min=eta_min, last_epoch=-1)
        return optimizer, scheduler